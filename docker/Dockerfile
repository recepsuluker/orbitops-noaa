FROM python:3.10-slim

# Non-root user
RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest/ ingest/

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "ingest/ingest_noaa.py"]
