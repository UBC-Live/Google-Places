import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from zoneinfo import ZoneInfo

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
LOCATION = os.getenv("GOOGLE_PLACES_LOCATION")      # "49.2606,-123.2460" for UBC
RADIUS = os.getenv("GOOGLE_PLACES_RADIUS")          # "500"
TYPE = os.getenv("GOOGLE_PLACES_TYPE", "cafe")      # default

if not API_KEY:
    raise ValueError("Missing GOOGLE_PLACES_API_KEY in .env")

BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Output directory
OUTPUT_DIR = "data/raw"


def fetch_google_places():
    """Fetch data from Google Places and save raw JSON to data/raw/"""

    # Vancouver time timestamp
    ts = datetime.now(ZoneInfo("America/Vancouver")).strftime("%Y-%m-%dT%H-%M-%S")

    params = {
        "location": LOCATION,
        "radius": RADIUS,
        "type": TYPE,
        "key": API_KEY
    }

    print(f"[{ts}] Sending request to Google Places API...")

    try:
        response = requests.get(BASE_URL, params=params)
        status = response.status_code

        if status != 200:
            print(f"[{ts}] ❌ API Error: Status Code {status}")
            return

        data = response.json()

        # Save snapshot of the response JSON
        snapshot_dir = "data/sample"
        os.makedirs(snapshot_dir, exist_ok=True)

        snapshot_path = os.path.join(snapshot_dir, f"{ts}.json")

        with open(snapshot_path, "w") as f:
            json.dump(data, f, indent=2)

        print(f"[{ts}] 📁 Saved snapshot to {snapshot_path}")

        # Create directory if missing
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Save raw JSON
        filename = f"google_places_{ts}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"[{ts}] ✅ Saved raw data to {filepath}")

    except Exception as e:
        print(f"[{ts}] ❌ Request failed: {e}")


if __name__ == "__main__":
    fetch_google_places()
