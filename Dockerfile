FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY calculadora/ calculadora/

RUN pip install --no-cache-dir . \
    && useradd --create-home appuser \
    && chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["calculadora"]