FROM python:3.12-slim

ENV PIP_ROOT_USER_ACTION=ignore \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv \
 && uv sync --no-dev --locked          


ENV PATH="/app/.venv/bin:$PATH"

COPY src ./src

EXPOSE 8080

CMD ["uvicorn", "src.api.v1.server:app", "--host", "0.0.0.0", "--port", "8080"]