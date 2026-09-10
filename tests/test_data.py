"""Tests for data loading, validation and splitting."""

from __future__ import annotations

import pandas as pd
import pytest

from alta_shared_task_2026 import data
from alta_shared_task_2026.constants import (
    REQUIRED_COLUMNS,
    SARCASM_COLUMN,
    SENTIMENT_COLUMN,
    TEXT_COLUMN,
)


def test_load_table_infers_separators(tmp_path) -> None:
    frame = pd.DataFrame({"a": [1, 2]})
    csv_path = tmp_path / "x.csv"
    tsv_path = tmp_path / "x.tsv"
    frame.to_csv(csv_path, index=False)
    frame.to_csv(tsv_path, sep="\t", index=False)

    assert data.load_table(csv_path)["a"].tolist() == [1, 2]
    assert data.load_table(tsv_path)["a"].tolist() == [1, 2]


def test_validate_keeps_required_columns(sample_frame) -> None:
    result = data.validate(sample_frame)
    assert set(REQUIRED_COLUMNS).issubset(result.columns)


def test_validate_rejects_missing_columns() -> None:
    with pytest.raises(data.DataError):
        data.validate(pd.DataFrame({TEXT_COLUMN: ["hello"]}))


def test_validate_rejects_non_binary_labels(sample_frame) -> None:
    bad = sample_frame.copy()
    bad.loc[0, SENTIMENT_COLUMN] = 2
    with pytest.raises(data.DataError):
        data.validate(bad)


def test_validate_require_variety_filters(sample_frame) -> None:
    result = data.validate(sample_frame, require_variety=True)
    assert set(result["variety"].unique()).issubset({"en-AU", "en-UK"})


def test_split_sizes_and_stratification(sample_frame) -> None:
    train, test, dev = data.split(sample_frame, test_size=0.2, dev_size=0.25)
    assert dev is not None
    assert len(train) + len(test) + len(dev) == len(sample_frame)
    for split_ in (train, test, dev):
        assert set(split_[SENTIMENT_COLUMN].unique()) == {0, 1}
        assert set(split_[SARCASM_COLUMN].unique()) == {0, 1}


def test_from_besstie_long(sample_frame) -> None:
    long_frame = pd.concat(
        [
            sample_frame[[TEXT_COLUMN, SENTIMENT_COLUMN, "variety", "source"]]
            .rename(columns={SENTIMENT_COLUMN: "label"})
            .assign(task="sentiment"),
            sample_frame[[TEXT_COLUMN, SARCASM_COLUMN]]
            .rename(columns={SARCASM_COLUMN: "label"})
            .assign(task="sarcasm"),
        ],
        ignore_index=True,
    )
    wide = data.from_besstie_long(long_frame)
    assert set(wide.columns) >= {TEXT_COLUMN, SENTIMENT_COLUMN, SARCASM_COLUMN}
    assert len(wide) == len(sample_frame)
