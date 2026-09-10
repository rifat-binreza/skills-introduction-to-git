"""Tests for the baseline classifier."""

from __future__ import annotations

import numpy as np

from alta_shared_task_2026 import models
from alta_shared_task_2026.constants import SARCASM_COLUMN, SENTIMENT_COLUMN, TEXT_COLUMN


def test_baseline_fit_and_predict(sample_frame) -> None:
    texts = sample_frame[TEXT_COLUMN].tolist()
    model = models.BaselineClassifier(min_df=1).fit(texts, sample_frame[SENTIMENT_COLUMN])
    predictions = model.predict(texts)

    assert predictions.shape == (len(texts),)
    assert set(np.unique(predictions)).issubset({0, 1})


def test_baseline_probabilities_sum_to_one(sample_frame) -> None:
    texts = sample_frame[TEXT_COLUMN].tolist()
    model = models.BaselineClassifier(min_df=1).fit(texts, sample_frame[SARCASM_COLUMN])
    probabilities = model.predict_proba(texts)

    np.testing.assert_allclose(probabilities.sum(axis=1), 1.0)


def test_baseline_roundtrip(tmp_path, sample_frame) -> None:
    texts = sample_frame[TEXT_COLUMN].tolist()
    model = models.BaselineClassifier(min_df=1).fit(texts, sample_frame[SENTIMENT_COLUMN])
    path = tmp_path / "sentiment.joblib"
    model.save(path)

    reloaded = models.BaselineClassifier.load(path)
    np.testing.assert_array_equal(model.predict(texts), reloaded.predict(texts))
