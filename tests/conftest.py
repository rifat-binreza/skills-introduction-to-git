"""Shared fixtures for the ALTA 2026 Shared Task test suite."""

from __future__ import annotations

import pandas as pd
import pytest

from alta_shared_task_2026.constants import (
    SARCASM_COLUMN,
    SENTIMENT_COLUMN,
    SOURCE_COLUMN,
    TEXT_COLUMN,
    VARIETY_COLUMN,
)

_POSITIVE = ["great", "love", "excellent", "wonderful", "fantastic"]
_NEGATIVE = ["terrible", "awful", "dreadful", "horrible", "bad"]
_SARCASTIC = ["totally", "obviously", "sure"]
_SINCERE = ["genuinely", "honestly", "really"]


@pytest.fixture
def sample_frame() -> pd.DataFrame:
    """Build a small, balanced, synthetic BESSTIE-style frame."""
    rows: list[dict[str, object]] = []
    for index in range(240):
        sentiment = index % 2
        sarcasm = (index // 2) % 2
        positive = _POSITIVE[index % len(_POSITIVE)]
        negative = _NEGATIVE[index % len(_NEGATIVE)]
        cue = _SARCASTIC[index % len(_SARCASTIC)] if sarcasm else _SINCERE[index % len(_SINCERE)]
        text = f"{positive if sentiment else negative} service {cue} {index}"
        rows.append(
            {
                TEXT_COLUMN: text,
                SENTIMENT_COLUMN: sentiment,
                SARCASM_COLUMN: sarcasm,
                VARIETY_COLUMN: "en-AU" if index % 2 == 0 else "en-UK",
                SOURCE_COLUMN: "GOOGLE" if index % 2 == 0 else "REDDIT",
            }
        )
    return pd.DataFrame(rows)
