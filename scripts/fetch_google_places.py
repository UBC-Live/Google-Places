import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

if not API_KEY:
    raise ValueError("Missing GOOGLE_PLACES_API_KEY in .env file.")

# Google Places Nearby Search endpoint
BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Default query (matches docs/access.md)
LOCATION = "49.2606,-123.2460"      # UBC
RADIUS = 500
TYPE = "cafe"

# Output directory (already exists in your repo)
OUTPUT_DIR = "data/raw"


def fetch_google_places():

    # Timestamp: YYYY-MM-DDTHH-MM-SS
    ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

    params = {
        "location": LOCATION,
        "radius": RADIUS,
        "type": TYPE,
        "key": API_KEY
    }

    print(f"[{ts}] Sending request to Google Places API...")

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        print(f"[{ts}] Status Code: {response.status_code}")

        if response.status_code != 200:
            print(f"[{ts}] Error: Non-200 response.")
            return

        data = response.json()

        filename = f"google_places_{ts}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"[{ts}] Saved raw data → {filepath}")

    except Exception as e:
        print(f"[{ts}] ERROR: {e}")


if __name__ == "__main__":
    fetch_google_places()
