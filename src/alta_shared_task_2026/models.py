"""Baseline classifiers for the ALTA 2026 Shared Task."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from alta_shared_task_2026.constants import RANDOM_STATE
from alta_shared_task_2026.preprocess import normalize_text


class BaselineClassifier:
    """A TF-IDF + logistic-regression baseline for a single binary task.

    The model is intentionally simple so that it can serve as a reproducible
    reference point: word bigrams are vectorised with TF-IDF and fed to an
    L2-regularised logistic regression.
    """

    def __init__(
        self,
        *,
        random_state: int = RANDOM_STATE,
        max_iter: int = 1000,
        **vectorizer_kwargs: Any,
    ) -> None:
        vectorizer_defaults: dict[str, Any] = {
            "preprocessor": normalize_text,
            "sublinear_tf": True,
            "ngram_range": (1, 2),
            "min_df": 2,
            "max_features": 50_000,
            "strip_accents": "unicode",
        }
        vectorizer_defaults.update(vectorizer_kwargs)
        self.pipeline = Pipeline(
            steps=[
                ("tfidf", TfidfVectorizer(**vectorizer_defaults)),
                ("clf", LogisticRegression(random_state=random_state, max_iter=max_iter)),
            ]
        )

    def fit(self, texts: Iterable[str], labels: Iterable[int]) -> BaselineClassifier:
        """Fit the pipeline to the given texts and binary labels."""
        self.pipeline.fit(list(texts), list(labels))
        return self

    def predict(self, texts: Iterable[str]) -> np.ndarray:
        """Return binary predictions for the given texts."""
        return self.pipeline.predict(list(texts))

    def predict_proba(self, texts: Iterable[str]) -> np.ndarray:
        """Return class probabilities for the given texts."""
        return self.pipeline.predict_proba(list(texts))

    def save(self, path: str | Path) -> None:
        """Persist the fitted pipeline to ``path`` with joblib."""
        joblib.dump(self.pipeline, path)

    @classmethod
    def load(cls, path: str | Path) -> BaselineClassifier:
        """Load a fitted pipeline previously saved with :meth:`save`."""
        model = cls.__new__(cls)
        model.pipeline = joblib.load(path)
        return model
