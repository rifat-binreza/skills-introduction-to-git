# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-09-10

### Added

- Baseline tooling for the ALTA 2026 Shared Task (sentiment and sarcasm
  classification across en-AU and en-UK BESSTIE subsets).
- `alta_shared_task_2026` Python package with data loading/validation, a
  TF-IDF + logistic-regression baseline, evaluation utilities and submission
  generation.
- `alta2026` CLI with `train`, `evaluate` and `predict` subcommands.
- Full unit test suite (`pytest`) with coverage reporting.
- Modern tooling: `pyproject.toml` (PEP 621), ruff, mypy, pre-commit, Makefile,
  Dockerfile, devcontainer, and GitHub Actions CI/release workflows.
- Project documentation (README, task guide, setup, contributing) and community
  files (code of conduct, security policy, citation metadata).

[Unreleased]: https://github.com/rifat-binreza/skills-introduction-to-git/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/rifat-binreza/skills-introduction-to-git/releases/tag/v0.1.0
