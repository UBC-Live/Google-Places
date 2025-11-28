import json
import pandas as pd
from datetime import datetime
import os


RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"


def load_latest_raw():
    """
    Load the most recent raw Google Places JSON file from data/raw/.

    Returns
    -------
    dict
        Parsed JSON dictionary from the newest raw ingestion file.

    Raises
    ------
    FileNotFoundError
        If no raw JSON files exist in data/raw/.
    """
    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".json")]
    if not files:
        raise FileNotFoundError("No raw ingestion files found in data/raw/")

    latest = max(files)  # newest file (based on timestamp in filename)
    filepath = os.path.join(RAW_DIR, latest)

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def clean_places(data):
    """
    Clean and flatten Google Places JSON results into a structured dataframe.

    This function:
    - Extracts coordinates from geometry.location
    - Converts types safely (float, int, bool)
    - Adds timestamps (ISO + yyyymmdd)
    - Flattens 'types' list into comma-separated string

    Parameters
    ----------
    data : dict
        JSON dictionary returned by load_latest_raw().

    Returns
    -------
    pandas.DataFrame
        A cleaned dataframe with standard schema and datatypes.
    """
    results = data.get("results", [])
    rows = []

    for item in results:
        lat = item.get("geometry", {}).get("location", {}).get("lat")
        lng = item.get("geometry", {}).get("location", {}).get("lng")
        open_now = item.get("opening_hours", {}).get("open_now")

        ts = datetime.now()
        yyyymmdd = int(ts.strftime("%Y%m%d"))

        cleaned = {
            "place_id": item.get("place_id"),
            "name": item.get("name"),
            "address": item.get("formatted_address") or item.get("vicinity"),
            "lat": float(lat) if lat is not None else None,
            "lng": float(lng) if lng is not None else None,
            "rating": float(item.get("rating")) if item.get("rating") else None,
            "user_ratings_total": int(item.get("user_ratings_total") or 0),
            "business_status": item.get("business_status"),
            "open_now": bool(open_now) if open_now is not None else None,
            "types": ", ".join(item.get("types", [])),
            "ts": ts.isoformat(),
            "yyyymmdd": yyyymmdd
        }

        rows.append(cleaned)

    return pd.DataFrame(rows)


def save_clean(df):
    """
    Save the cleaned dataframe to data/clean/places_clean.json.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned dataframe produced by clean_places().
    """
    os.makedirs(CLEAN_DIR, exist_ok=True)

    output_path = os.path.join(CLEAN_DIR, "places_clean.json")
    df.to_json(output_path, orient="records", indent=2)


if __name__ == "__main__":
    raw = load_latest_raw()
    df = clean_places(raw)
    save_clean(df)
