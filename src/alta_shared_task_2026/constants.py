"""Shared constants for the ALTA 2026 Shared Task."""

from __future__ import annotations

TEXT_COLUMN = "text"
VARIETY_COLUMN = "variety"
SOURCE_COLUMN = "source"

SENTIMENT_COLUMN = "sentiment"
SARCASM_COLUMN = "sarcasm"
TASK_COLUMNS = (SENTIMENT_COLUMN, SARCASM_COLUMN)

REQUIRED_COLUMNS = (TEXT_COLUMN, SENTIMENT_COLUMN, SARCASM_COLUMN)

# Label spaces for the two binary tasks.
SENTIMENT_LABELS = {0: "negative", 1: "positive"}
SARCASM_LABELS = {0: "not_sarcastic", 1: "sarcastic"}

# The 2026 shared task targets these two BESSTIE varieties.
TARGET_VARIETIES = ("en-AU", "en-UK")

SUBMISSION_COLUMNS = ("id", SENTIMENT_COLUMN, SARCASM_COLUMN)

RANDOM_STATE = 42
DEFAULT_TEST_SIZE = 0.2
DEFAULT_DEV_SIZE = 0.2
