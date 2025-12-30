FROM python:3.10-slim

RUN useradd -m appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest/ ingest/
RUN chown -R appuser:appuser /app

USER appuser
CMD ["python3", "ingest/ingest_noaa.py"]

