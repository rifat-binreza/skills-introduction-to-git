# Setup Guide

This guide covers setting up a development environment for the **ALTA Shared
Task 2026** baseline.

## Prerequisites

- **Python 3.10+** (tested on 3.10–3.12)
- **Git**
- Optional: [uv](https://docs.astral.sh/uv/), [Docker](https://www.docker.com/),
  or VS Code with the
  [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
  extension.

## Option A: `uv` (recommended)

`uv` manages the virtual environment and dependencies in one step.

```bash
# Install uv if you don't have it:
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git

uv sync --extra dev        # create .venv, install package + dev tooling
uv run pytest              # run tests
uv run alta2026 --help     # use the CLI
```

## Option B: `pip` + venv

```bash
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install -e ".[dev]"

pytest                             # run tests
alta2026 --help                    # use the CLI
```

## Option C: Docker

```bash
git clone https://github.com/rifat-binreza/skills-introduction-to-git.git
cd skills-introduction-to-git

docker build -t alta-shared-task-2026 .
docker run --rm alta-shared-task-2026 --help
```

## Option D: Devcontainer / Codespaces

1. Open the repository in VS Code.
2. Install the Dev Containers extension and reopen in container
   (or open it in GitHub Codespaces).
3. The devcontainer installs Python 3.12, the `dev` dependencies and pre-commit
   hooks automatically.

## Install the pre-commit hooks

Once the `dev` dependencies are installed, enable the git hooks:

```bash
pre-commit install
```

Lint, formatting and type-checking will now run automatically on every commit.

## Verify your environment

```bash
make check    # runs lint (ruff + mypy) and the test suite
```

Individual targets:

| Command | What it does |
| --- | --- |
| `make lint` | `ruff check`, `ruff format --check`, `mypy` |
| `make format` | Auto-format and auto-fix |
| `make test` | Run `pytest` |
| `make test-cov` | Run tests with coverage |
| `make build` | Build sdist and wheel |

## Troubleshooting

**`alta2026: command not found`** — the package isn't installed. Re-run
`pip install -e ".[dev]"` (or `uv sync --extra dev`) and make sure your virtual
environment is active.

**`ModuleNotFoundError: No module named 'datasets'`** — the Hugging Face extras
aren't installed. Run `pip install -e ".[hf]"`.

**Slow first `uv sync`** — uv needs to resolve and download packages once;
subsequent runs are cached.
