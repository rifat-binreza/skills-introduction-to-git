"""Text-normalisation utilities for the ALTA 2026 Shared Task."""

from __future__ import annotations

import re
import unicodedata

import pandas as pd

_WHITESPACE_RE = re.compile(r"\s+")
_HANDLE_RE = re.compile(r"@\w+")
_URL_RE = re.compile(r"https?://\S+|www\.\S+")


def normalize_text(
    text: str,
    *,
    strip_handles: bool = False,
    strip_urls: bool = False,
) -> str:
    """Normalise a single text sample.

    Applies Unicode NFKC normalisation, lowercases and collapses all runs of
    whitespace. ``@handles`` and URLs can optionally be removed.
    """
    text = unicodedata.normalize("NFKC", str(text)).lower()
    if strip_handles:
        text = _HANDLE_RE.sub(" ", text)
    if strip_urls:
        text = _URL_RE.sub(" ", text)
    return _WHITESPACE_RE.sub(" ", text).strip()


def normalize_series(series: pd.Series) -> pd.Series:
    """Apply :func:`normalize_text` element-wise to a pandas Series."""
    return series.map(normalize_text)
