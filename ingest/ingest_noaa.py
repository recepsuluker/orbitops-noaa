import requests
import json
from datetime import datetime
import os

URL = "https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"
OUT = os.environ.get("OUTPUT_PATH", "/app/output/latest.json")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
r = requests.get(URL, timeout=10)
r.raise_for_status()

data = r.json()

payload = {
    "ingested_at": datetime.utcnow().isoformat(),
    "records": len(data),
    "latest": data[-1]
}

with open(OUT, "w") as f:
    json.dump(payload, f, indent=2)

print("NOAA ingestion successful")
