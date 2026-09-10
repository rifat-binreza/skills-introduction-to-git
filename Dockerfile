# ---------------------------------------------------------------------------
# Build stage: create a wheel in an isolated layer.
# ---------------------------------------------------------------------------
FROM python:3.12-slim AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

COPY pyproject.toml README.md LICENSE ./
COPY src ./src

RUN pip install --upgrade pip \
    && pip install build \
    && python -m build --wheel

# ---------------------------------------------------------------------------
# Runtime stage: install only the wheel and drop privileges.
# ---------------------------------------------------------------------------
FROM python:3.12-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN useradd --create-home --uid 10001 appuser

COPY --from=builder /build/dist/*.whl ./wheel/
RUN pip install --upgrade pip \
    && pip install ./wheel/*.whl \
    && rm -rf ./wheel

USER appuser

ENTRYPOINT ["alta2026"]
