"""End-to-end CLI tests."""

from __future__ import annotations

import pandas as pd

from alta_shared_task_2026 import cli


def test_train_and_predict_end_to_end(tmp_path, sample_frame) -> None:
    train_path = tmp_path / "train.csv"
    test_path = tmp_path / "test.csv"
    sample_frame.to_csv(train_path, index=False)
    sample_frame.drop(columns=["sentiment", "sarcasm"]).to_csv(test_path, index=False)
    model_dir = tmp_path / "models"

    assert (
        cli.main(
            ["train", "--train", str(train_path), "--model-dir", str(model_dir), "--min-df", "1"]
        )
        == 0
    )

    output = tmp_path / "submission.csv"
    assert (
        cli.main(
            [
                "predict",
                "--model-dir",
                str(model_dir),
                "--test",
                str(test_path),
                "--output",
                str(output),
            ]
        )
        == 0
    )

    back = pd.read_csv(output)
    assert list(back.columns) == ["id", "sentiment", "sarcasm"]
    assert len(back) == len(sample_frame)
