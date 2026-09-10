# ALTA Shared Task 2026 — developer convenience targets.
# Requires Python 3.10+ and pip (or uv, see `make install-uv`).

PY ?= python3
PIP ?= $(PY) -m pip

.DEFAULT_GOAL := help

.PHONY: help install install-dev install-uv lock lint format check test test-cov build docker-build docker-run clean

help: ## Show this help message
	@printf "ALTA Shared Task 2026\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

install: ## Install the package (editable, no dev tools)
	$(PIP) install -e .

install-dev: ## Install the package plus dev tooling
	$(PIP) install -e ".[dev]"

install-uv: ## Sync dependencies with uv (fast, reproducible)
	uv sync --extra dev

lock: ## Freeze dependencies into uv.lock
	uv lock

lint: ## Run the linter and type checker
	ruff check src tests
	ruff format --check src tests
	mypy src

format: ## Auto-format and auto-fix lint issues
	ruff format src tests
	ruff check --fix src tests

check: lint test ## Run the full local CI gate

test: ## Run the test suite
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=alta_shared_task_2026 --cov-report=term-missing

build: ## Build sdist and wheel
	$(PY) -m build

docker-build: ## Build the container image
	docker build -t alta-shared-task-2026 .

docker-run: ## Run the CLI inside the container
	docker run --rm alta-shared-task-2026 --help

clean: ## Remove build and cache artifacts
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
