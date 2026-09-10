"""Tests for submission-file generation."""

from __future__ import annotations

import pandas as pd
import pytest

from alta_shared_task_2026 import submission


def test_build_submission_schema() -> None:
    frame = submission.build_submission([1, 2, 3], [0, 1, 0], [1, 0, 0])
    assert list(frame.columns) == ["id", "sentiment", "sarcasm"]
    assert frame["id"].tolist() == [1, 2, 3]


def test_write_submission_roundtrip(tmp_path) -> None:
    frame = submission.build_submission([1, 2], [0, 1], [1, 0])
    out = submission.write_submission(frame, tmp_path / "submission.csv")

    back = pd.read_csv(out)
    assert list(back.columns) == ["id", "sentiment", "sarcasm"]
    assert back["id"].tolist() == [1, 2]


def test_write_submission_rejects_missing_column(tmp_path) -> None:
    with pytest.raises(ValueError):
        submission.write_submission(pd.DataFrame({"id": [1], "sentiment": [0]}), tmp_path / "x.csv")
