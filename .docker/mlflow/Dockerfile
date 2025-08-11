FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv && \
    uv pip install --system "mlflow[extras]==2.14.1" boto3 psycopg2-binary

EXPOSE 5000