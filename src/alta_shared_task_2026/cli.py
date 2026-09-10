"""Command-line interface for the ALTA 2026 Shared Task baseline."""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path

import pandas as pd

from alta_shared_task_2026 import __version__
from alta_shared_task_2026.constants import (
    RANDOM_STATE,
    SARCASM_COLUMN,
    SENTIMENT_COLUMN,
    TEXT_COLUMN,
)
from alta_shared_task_2026.data import DataError, load_table, split, validate
from alta_shared_task_2026.evaluate import evaluate_frame
from alta_shared_task_2026.models import BaselineClassifier
from alta_shared_task_2026.submission import build_submission, write_submission


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level argument parser."""
    parser = argparse.ArgumentParser(
        prog="alta2026",
        description="Baseline tooling for the ALTA 2026 Shared Task (sentiment and sarcasm).",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    train = subparsers.add_parser("train", help="Train baseline classifiers and save them.")
    train.add_argument("--train", required=True, type=Path, help="Path to the training CSV/TSV.")
    train.add_argument("--dev", type=Path, help="Optional development CSV/TSV.")
    train.add_argument(
        "--model-dir", type=Path, default=Path("models"), help="Where to save models."
    )
    train.add_argument("--seed", type=int, default=RANDOM_STATE)
    train.add_argument(
        "--min-df", type=int, default=2, help="Minimum document frequency for TF-IDF."
    )

    predict = subparsers.add_parser("predict", help="Generate a submission file.")
    predict.add_argument("--model-dir", type=Path, default=Path("models"))
    predict.add_argument("--test", required=True, type=Path, help="Path to unlabelled test data.")
    predict.add_argument("--output", type=Path, default=Path("submission.csv"))
    predict.add_argument("--sep", default=",", help="Output separator (default: comma).")

    evaluate = subparsers.add_parser("evaluate", help="Evaluate saved models on labelled data.")
    evaluate.add_argument("--model-dir", type=Path, default=Path("models"))
    evaluate.add_argument(
        "--data", required=True, type=Path, help="Path to labelled evaluation data."
    )
    evaluate.add_argument("--by-variety", action="store_true", help="Report metrics per variety.")

    return parser


def _train(args: argparse.Namespace) -> int:
    train = validate(load_table(args.train))
    if args.dev is not None:
        dev = validate(load_table(args.dev))
    else:
        train, dev, _ = split(train, test_size=0.2, dev_size=None, random_state=args.seed)

    args.model_dir.mkdir(parents=True, exist_ok=True)
    models: dict[str, BaselineClassifier] = {}
    for task in (SENTIMENT_COLUMN, SARCASM_COLUMN):
        model = BaselineClassifier(random_state=args.seed, min_df=args.min_df).fit(
            train[TEXT_COLUMN], train[task]
        )
        model.save(args.model_dir / f"{task}.joblib")
        models[task] = model

    report = evaluate_frame(
        dev,
        sentiment_pred=models[SENTIMENT_COLUMN].predict(dev[TEXT_COLUMN]),
        sarcasm_pred=models[SARCASM_COLUMN].predict(dev[TEXT_COLUMN]),
        by_variety=True,
    )
    print("Development-set results:")
    print(report.to_string(index=False))
    return 0


def _predict(args: argparse.Namespace) -> int:
    test = load_table(args.test)
    if TEXT_COLUMN not in test.columns:
        raise DataError(f"Test data must contain a '{TEXT_COLUMN}' column.")
    ids = test["id"] if "id" in test.columns else pd.RangeIndex(1, len(test) + 1)

    predictions: dict[str, list[int]] = {}
    for task in (SENTIMENT_COLUMN, SARCASM_COLUMN):
        model = BaselineClassifier.load(args.model_dir / f"{task}.joblib")
        predictions[task] = [int(value) for value in model.predict(test[TEXT_COLUMN])]

    submission = build_submission(ids, predictions[SENTIMENT_COLUMN], predictions[SARCASM_COLUMN])
    output = write_submission(submission, args.output, sep=args.sep)
    print(f"Wrote {len(submission)} predictions to {output}")
    return 0


def _evaluate(args: argparse.Namespace) -> int:
    frame = validate(load_table(args.data))
    predictions: dict[str, list[int]] = {}
    for task in (SENTIMENT_COLUMN, SARCASM_COLUMN):
        model = BaselineClassifier.load(args.model_dir / f"{task}.joblib")
        predictions[task] = [int(value) for value in model.predict(frame[TEXT_COLUMN])]

    report = evaluate_frame(
        frame,
        sentiment_pred=predictions[SENTIMENT_COLUMN],
        sarcasm_pred=predictions[SARCASM_COLUMN],
        by_variety=args.by_variety,
    )
    print(report.to_string(index=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return an exit code."""
    args = build_parser().parse_args(argv)
    handlers: dict[str, Callable[[argparse.Namespace], int]] = {
        "train": _train,
        "predict": _predict,
        "evaluate": _evaluate,
    }
    return handlers[args.command](args)
