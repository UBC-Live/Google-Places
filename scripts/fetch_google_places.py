import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from zoneinfo import ZoneInfo

# Load environment variables
load_dotenv()

# Default values retrieved from environment variables
DEFAULT_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
DEFAULT_LOCATION = os.getenv("GOOGLE_PLACES_LOCATION")      # e.g. "49.2606,-123.2460" for UBC
DEFAULT_RADIUS = os.getenv("GOOGLE_PLACES_RADIUS")          # e.g. "500"
DEFAULT_TYPE = os.getenv("GOOGLE_PLACES_TYPE", "cafe")      # default place type

if not DEFAULT_API_KEY:
    raise ValueError("Missing GOOGLE_PLACES_API_KEY in .env")

BASE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
OUTPUT_DIR = "data/raw"


def fetch_google_places(
    api_key: str = DEFAULT_API_KEY,
    location: str = DEFAULT_LOCATION,
    radius: str = DEFAULT_RADIUS,
    place_type: str = DEFAULT_TYPE
):
    """
    Fetch data from the Google Places Nearby Search API and save raw JSON output.

    Parameters
    ----------
    api_key : str
        Your Google Places API key. Defaults to GOOGLE_PLACES_API_KEY from .env.
    location : str
        Latitude and longitude in `"lat,lng"` format. Represents the center point
        from which the API searches. Defaults to GOOGLE_PLACES_LOCATION from .env.
    radius : str
        Search radius in meters around the location. Defaults to GOOGLE_PLACES_RADIUS from .env.
    place_type : str
        Type of place to search for (e.g., "cafe", "restaurant", "library").
        Determines what category the API filters results to.
        Defaults to GOOGLE_PLACES_TYPE from .env.

    Notes
    -----
    - TYPE is used by Google Places to filter to a specific category.
      For example, TYPE="cafe" returns only coffee shops.
    - Response snapshots are saved in `data/sample/` for schema inspection.
    - Full raw ingestion is saved in `data/raw/` for downstream processing.
    """

    # Vancouver timestamp
    ts = datetime.now(ZoneInfo("America/Vancouver")).strftime("%Y-%m-%dT%H-%M-%S")

    params = {
        "location": location,
        "radius": radius,
        "type": place_type,
        "key": api_key
    }

    print(f"[{ts}] Sending request to Google Places API...")

    try:
        response = requests.get(BASE_URL, params=params)
        status = response.status_code

        if status != 200:
            print(f"[{ts}] ❌ API Error: Status Code {status}")
            return

        data = response.json()

        # Save sample snapshot for schema review
        snapshot_dir = "data/sample"
        os.makedirs(snapshot_dir, exist_ok=True)
        snapshot_path = os.path.join(snapshot_dir, f"{ts}.json")
        with open(snapshot_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[{ts}] 📁 Saved snapshot to {snapshot_path}")

        # Save full raw ingestion
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        raw_filename = f"google_places_{ts}.json"
        raw_filepath = os.path.join(OUTPUT_DIR, raw_filename)
        with open(raw_filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(f"[{ts}] ✅ Saved raw data to {raw_filepath}")

    except Exception as e:
        print(f"[{ts}] ❌ Request failed: {e}")


if __name__ == "__main__":
    fetch_google_places()
