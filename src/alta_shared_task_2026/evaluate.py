"""Evaluation utilities for the ALTA 2026 Shared Task."""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from alta_shared_task_2026.constants import SARCASM_COLUMN, SENTIMENT_COLUMN, VARIETY_COLUMN

_METRIC_COLUMNS = ("accuracy", "precision", "recall", "f1_macro")


def binary_metrics(y_true: Iterable[int], y_pred: Iterable[int]) -> dict[str, float]:
    """Compute accuracy and macro precision/recall/F1 for a binary task."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }


def evaluate_frame(
    frame: pd.DataFrame,
    *,
    sentiment_pred: Iterable[int],
    sarcasm_pred: Iterable[int],
    by_variety: bool = False,
) -> pd.DataFrame:
    """Return a tidy table of metrics for both tasks, optionally per variety."""
    frame = frame.copy()
    frame["sentiment_pred"] = list(sentiment_pred)
    frame["sarcasm_pred"] = list(sarcasm_pred)

    groups: list[str | None] = [None]
    if by_variety and VARIETY_COLUMN in frame.columns:
        groups += [str(variety) for variety in sorted(frame[VARIETY_COLUMN].dropna().unique())]

    rows: list[dict[str, object]] = []
    for group in groups:
        subset = frame if group is None else frame[frame[VARIETY_COLUMN] == group]
        for task in (SENTIMENT_COLUMN, SARCASM_COLUMN):
            row: dict[str, object] = {
                "variety": "overall" if group is None else group,
                "task": task,
            }
            row.update(binary_metrics(subset[task], subset[f"{task}_pred"]))
            rows.append(row)
    return pd.DataFrame(rows)[["variety", "task", *_METRIC_COLUMNS]]
