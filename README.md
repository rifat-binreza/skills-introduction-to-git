# ALTA Shared Task 2026

_Baseline and tooling for the **ALTA 2026 Shared Task**: joint **sentiment** and
**sarcasm** classification across **Australian (en-AU)** and **British (en-UK)**
English, using the [BESSTIE](https://huggingface.co/datasets/unswnlporg/BESSTIE)
benchmark._

<p align="center">
  <a href="https://github.com/rifat-binreza/skills-introduction-to-git/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/rifat-binreza/skills-introduction-to-git/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/rifat-binreza/skills-introduction-to-git/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://www.python.org/downloads/"><img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-blue.svg"></a>
  <a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
</p>

---

## The task

The seventeenth ALTA programming competition asks participants to build a system
that, for a given piece of **Australian** or **British** English text, predicts
two labels:

| Task | Labels |
| --- | --- |
| **Sentiment** | `0` negative · `1` positive |
| **Sarcasm** | `0` not sarcastic · `1` sarcastic |

Systems are evaluated on the **en-AU** and **en-UK** subsets of
[BESSTIE](https://aclanthology.org/2025.findings-acl.441/) (Srirag et al.,
2025) and are expected to remain **robust across both English varieties**.

### Key dates

| Milestone | Date |
| --- | --- |
| Registration & training/dev data release | Open (28 July 2026) |
| Test data release | 22 September 2026 |
| Submission of runs | 28 September 2026 |
| Notification of results | 1 October 2026 |
| System description due | 26 October 2026 |
| Camera-ready due | 2 November 2026 |
| Presentation at ALTA 2026 (Melbourne) | 30 Nov – 2 Dec 2026 |

- **Organisers**: coordinator Diego Mollá-Aliod (Macquarie University); data
  Aditya Joshi & Dipankar Srirag (UNSW).
- **Contact**: <shared.task@alta.asn.au> · **Prize**: $500 AUD.
- **Register / full details**: <https://www.alta.asn.au/events/sharedtask2026/>

---

## Quick start

### With `uv` (recommended)

```bash
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git

uv sync --extra dev       # install the package + dev tooling in a venv
uv run alta2026 --help    # verify the CLI
```

### With `pip`

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
alta2026 --help
```

### With Docker

```bash
docker build -t alta-shared-task-2026 .
docker run --rm alta-shared-task-2026 --help
```

### With a devcontainer / Codespaces

Open the repository in VS Code with the
[Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
extension — `.devcontainer/devcontainer.json` provisions Python 3.12, ruff,
mypy and pre-commit automatically.

---

## Usage

The `alta2026` CLI has three subcommands.

```bash
# Train baselines; the dev set is held out automatically if --dev is omitted.
alta2026 train --train data/processed/train.csv \
               --dev data/processed/dev.csv \
               --model-dir models

# Score a labelled evaluation set (optionally broken down per variety).
alta2026 evaluate --model-dir models --data data/processed/dev.csv --by-variety

# Produce a submission file from unlabelled test data.
alta2026 predict --model-dir models \
                 --test data/raw/test.csv \
                 --output submission.csv
```

The data schema is `text` plus binary `sentiment` and `sarcasm` columns, with
optional `variety` (`en-AU`/`en-UK`) and `source` columns (CSV, TSV or Parquet).

### The baseline

The reference model is a scikit-learn pipeline: **word bigrams → TF-IDF →
L2-regularised logistic regression**, trained independently per task. It is
deliberately simple and reproducible so it can serve as the floor that fancier
systems (fine-tuned LLMs, ensemble models, …) must beat.

---

## Repository structure

```
.
├── .devcontainer/            # VS Code devcontainer / Codespaces config
├── .github/
│   ├── workflows/            # CI (lint → test matrix → build) + release
│   ├── ISSUE_TEMPLATE/       # Bug & feature issue forms
│   ├── CODEOWNERS
│   ├── dependabot.yml
│   └── pull_request_template.md
├── docs/
│   ├── TASK.md               # Detailed task guide
│   ├── SETUP.md              # Setup & environment guide
│   └── CONTRIBUTING.md       # Contribution guidelines
├── src/alta_shared_task_2026/
│   ├── cli.py                # alta2026 command-line interface
│   ├── data.py               # Loading, validation, splitting
│   ├── models.py             # TF-IDF + logistic-regression baseline
│   ├── evaluate.py           # Metrics & per-variety breakdowns
│   ├── submission.py         # Submission-file generation
│   ├── preprocess.py         # Text normalisation
│   └── constants.py          # Columns, labels, defaults
├── tests/                    # pytest suite
├── data/                     # (git-ignored) raw/processed data
├── pyproject.toml            # Packaging + ruff/mypy/pytest config
├── Makefile                  # Common developer targets
├── Dockerfile                # Multi-stage container image
├── .pre-commit-config.yaml   # Pre-commit hooks (ruff, mypy, hygiene)
├── CITATION.cff              # Citation metadata
└── README.md
```

---

## Development

```bash
make install-dev   # pip install -e ".[dev]"
make lint          # ruff check + ruff format --check + mypy
make test          # pytest
make test-cov      # pytest with coverage
make check         # lint + test (the CI gate)
make build         # sdist + wheel
```

CI runs on every push and pull request:

1. **Lint & type-check** — `ruff`, `ruff format --check`, `mypy`.
2. **Test** — `pytest` with coverage across Python 3.10–3.12.
3. **Build** — builds the sdist and wheel.

Tagging a release (`v*`) triggers the release workflow to attach the built
distributions to a GitHub release.

---

## Documentation

- **[Task guide](docs/TASK.md)** — the shared task in detail, data and submission notes.
- **[Setup](docs/SETUP.md)** — environment setup (uv, pip, Docker, devcontainer).
- **[Contributing](docs/CONTRIBUTING.md)** — guidelines, commit conventions, workflow.

## Citation

If you use this code, please cite the BESSTIE benchmark (see
[`CITATION.cff`](CITATION.cff)):

```bibtex
@inproceedings{srirag-etal-2025-besstie,
    title = "{BESSTIE}: A Benchmark for Sentiment and Sarcasm Classification for Varieties of {E}nglish",
    author = "Srirag, Dipankar and Joshi, Aditya and Painter, Jordan and Kanojia, Diptesh",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    doi = "10.18653/v1/2025.findings-acl.441",
    pages = "8413--8429",
}
```

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE).
The BESSTIE dataset is distributed separately under **CC-BY-NC-4.0**; please
respect its terms and the shared task's rules.
