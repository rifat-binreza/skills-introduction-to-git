"""Submission-file generation for the ALTA 2026 Shared Task."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import pandas as pd

from alta_shared_task_2026.constants import SARCASM_COLUMN, SENTIMENT_COLUMN, SUBMISSION_COLUMNS


def build_submission(
    ids: Iterable[int],
    sentiment_pred: Iterable[int],
    sarcasm_pred: Iterable[int],
) -> pd.DataFrame:
    """Assemble predictions into the submission schema (id, sentiment, sarcasm)."""
    return pd.DataFrame(
        {
            "id": list(ids),
            SENTIMENT_COLUMN: [int(value) for value in sentiment_pred],
            SARCASM_COLUMN: [int(value) for value in sarcasm_pred],
        }
    )


def write_submission(frame: pd.DataFrame, path: str | Path, *, sep: str = ",") -> Path:
    """Write a submission frame to disk after validating its schema."""
    path = Path(path)
    missing = [column for column in SUBMISSION_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"Submission frame is missing columns: {', '.join(missing)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    frame[list(SUBMISSION_COLUMNS)].to_csv(path, sep=sep, index=False)
    return path
