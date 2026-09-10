"""Loading, validating and splitting data for the ALTA 2026 Shared Task."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.model_selection import train_test_split

from alta_shared_task_2026.constants import (
    DEFAULT_DEV_SIZE,
    DEFAULT_TEST_SIZE,
    RANDOM_STATE,
    REQUIRED_COLUMNS,
    SARCASM_COLUMN,
    SENTIMENT_COLUMN,
    TARGET_VARIETIES,
    TEXT_COLUMN,
    VARIETY_COLUMN,
)


class DataError(ValueError):
    """Raised when the input data does not conform to the expected schema."""


def load_table(path: str | Path, *, sep: str | None = None, **read_kwargs: Any) -> pd.DataFrame:
    """Read a CSV, TSV or Parquet file into a DataFrame.

    The separator is inferred from the file extension unless ``sep`` is given:
    ``.tsv`` uses a tab and ``.parquet`` uses the Parquet engine.
    """
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".parquet":
        return pd.read_parquet(path, **read_kwargs)
    if sep is None:
        sep = "\t" if suffix == ".tsv" else ","
    return pd.read_csv(path, sep=sep, **read_kwargs)


def validate(frame: pd.DataFrame, *, require_variety: bool = False) -> pd.DataFrame:
    """Validate a BESSTIE frame and return a normalised copy.

    Raises :class:`DataError` unless the frame contains the required columns
    (``text``, ``sentiment``, ``sarcasm``), non-empty text and binary (0/1)
    labels. When ``require_variety`` is set, only the target varieties are kept.
    """
    missing = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing:
        raise DataError(f"Missing required column(s): {', '.join(missing)}")

    result = frame.copy()
    result[TEXT_COLUMN] = result[TEXT_COLUMN].astype("string")
    if result[TEXT_COLUMN].isna().any():
        raise DataError("Found missing values in the text column.")
    result = result[result[TEXT_COLUMN].str.strip().ne("")]

    for column in (SENTIMENT_COLUMN, SARCASM_COLUMN):
        try:
            result[column] = result[column].astype(int)
        except (TypeError, ValueError) as exc:
            raise DataError(f"Column '{column}' must contain integer labels.") from exc
        if not set(result[column].unique()).issubset({0, 1}):
            raise DataError(f"Column '{column}' must only contain binary labels (0 or 1).")

    if require_variety:
        if VARIETY_COLUMN not in result.columns:
            raise DataError(f"Column '{VARIETY_COLUMN}' is required when require_variety is set.")
        result = result[result[VARIETY_COLUMN].isin(TARGET_VARIETIES)]

    return result.reset_index(drop=True)


def _stratify_key(frame: pd.DataFrame) -> pd.Series:
    """Build a combined label key used for stratified splitting."""
    return frame[SENTIMENT_COLUMN].astype(str) + "_" + frame[SARCASM_COLUMN].astype(str)


def split(
    frame: pd.DataFrame,
    *,
    test_size: float = DEFAULT_TEST_SIZE,
    dev_size: float | None = DEFAULT_DEV_SIZE,
    random_state: int = RANDOM_STATE,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame | None]:
    """Split a frame into train/test (and optionally dev) sets.

    Splits are stratified on the combined ``(sentiment, sarcasm)`` label pair so
    that every label combination is represented in each split. Returns
    ``(train, test, dev)`` where ``dev`` is ``None`` when ``dev_size`` is
    ``None``.
    """
    train, test = train_test_split(
        frame,
        test_size=test_size,
        random_state=random_state,
        stratify=_stratify_key(frame),
    )
    if dev_size is None:
        return train.reset_index(drop=True), test.reset_index(drop=True), None

    train, dev = train_test_split(
        train,
        test_size=dev_size,
        random_state=random_state,
        stratify=_stratify_key(train),
    )
    return train.reset_index(drop=True), test.reset_index(drop=True), dev.reset_index(drop=True)


def from_besstie_long(frame: pd.DataFrame) -> pd.DataFrame:
    """Convert the public long-format BESSTIE snapshot to the task schema.

    The Hugging Face snapshot of `BESSTIE`_ stores one row per ``(text, task)``
    with columns ``text``, ``label``, ``variety``, ``source`` and ``task``.
    This pivots it into one row per text with ``sentiment`` and ``sarcasm``
    columns, keeping ``variety`` and ``source`` when present.

    .. _BESSTIE: https://huggingface.co/datasets/unswnlporg/BESSTIE
    """
    required = {"text", "label", "task"}
    missing = required - set(frame.columns)
    if missing:
        raise DataError(f"Missing required column(s): {', '.join(sorted(missing))}")
    tasks = set(frame["task"].unique())
    if not {"sentiment", "sarcasm"}.issubset(tasks):
        raise DataError("Expected 'task' to contain 'sentiment' and 'sarcasm'.")

    keep = [column for column in ("variety", "source") if column in frame.columns]
    sentiment = frame[frame["task"] == "sentiment"][[*keep, "text", "label"]].rename(
        columns={"label": SENTIMENT_COLUMN}
    )
    sarcasm = frame[frame["task"] == "sarcasm"][["text", "label"]].rename(
        columns={"label": SARCASM_COLUMN}
    )
    wide = sentiment.merge(sarcasm, on="text", how="inner")
    return wide.reset_index(drop=True)


def load_huggingface(name: str = "unswnlporg/BESSTIE", *, split: str = "train") -> pd.DataFrame:
    """Load a dataset from the Hugging Face Hub (requires the ``hf`` extra)."""
    try:
        from datasets import load_dataset
    except ImportError as exc:
        raise ImportError(
            "Loading from the Hub requires the 'hf' extra: "
            "`pip install 'alta-shared-task-2026[hf]'`"
        ) from exc
    return load_dataset(name, split=split).to_pandas()
