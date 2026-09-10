"""Tests for evaluation utilities."""

from __future__ import annotations

from alta_shared_task_2026 import evaluate
from alta_shared_task_2026.constants import SARCASM_COLUMN, SENTIMENT_COLUMN


def test_binary_metrics_perfect() -> None:
    metrics = evaluate.binary_metrics([0, 0, 1, 1], [0, 0, 1, 1])
    assert metrics == {"accuracy": 1.0, "precision": 1.0, "recall": 1.0, "f1_macro": 1.0}


def test_binary_metrics_known_values() -> None:
    metrics = evaluate.binary_metrics([0, 0, 1, 1], [0, 1, 0, 1])
    assert metrics["accuracy"] == 0.5


def test_evaluate_frame_reports_both_tasks(sample_frame) -> None:
    table = evaluate.evaluate_frame(
        sample_frame,
        sentiment_pred=sample_frame[SENTIMENT_COLUMN].tolist(),
        sarcasm_pred=sample_frame[SARCASM_COLUMN].tolist(),
        by_variety=True,
    )
    assert set(table["task"].unique()) == {"sentiment", "sarcasm"}
    overall = table[table["variety"] == "overall"]
    assert (overall["f1_macro"] == 1.0).all()
