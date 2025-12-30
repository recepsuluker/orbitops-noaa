import os
from datetime import datetime
import json
import requests

OUT = os.getenv(
    "NOAA_OUTPUT",
    "/data/latest.json"
)

URL = "https://services.swpc.noaa.gov/products/summary/solar-wind.json"

r = requests.get(URL, timeout=10)
data = r.json()

payload = {
    "ingested_at": datetime.utcnow().isoformat(),
    "records": len(data),
    "latest": data[-1] if data else None
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)

with open(OUT, "w") as f:
    json.dump(payload, f, indent=2)

print("NOAA ingestion successful")

