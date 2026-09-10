"""Baseline tooling for the ALTA 2026 Shared Task.

The 2026 ALTA Shared Task asks participants to classify the **sentiment**
(positive/negative) and **sarcasm** (sarcastic/not sarcastic) of Australian
(en-AU) and British (en-UK) English text, using the corresponding subsets of the
`BESSTIE`_ benchmark, while remaining robust across both varieties.

.. _BESSTIE: https://huggingface.co/datasets/unswnlporg/BESSTIE
"""

from __future__ import annotations

from alta_shared_task_2026 import data, evaluate, models, preprocess, submission

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "data",
    "evaluate",
    "models",
    "preprocess",
    "submission",
]
