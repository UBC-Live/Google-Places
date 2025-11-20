# Google-Places
Uses the Google Places API to get information about on campus buildings 

# Google Places Real-Time Data Ingestion — UBC LIVE

This repository collects and organizes real-time place data (e.g., Starbucks, Tim Hortons, campus cafés) using the Google Places API.  
It is part of the **UBC LIVE** project, which supports lineup prediction, campus flow analysis, and real-time operational insights.

## 📌 What This Repo Does
- Fetches Google Places API data for selected UBC campus locations  
- Stores raw API responses in `/data/raw/`  
- Cleans and standardizes data into `/data/clean/`  
- Contains ingestion scripts in `/scripts/`  
- Stores documentation in `/docs/`

  
```markdown
## 📁 Folder Layout
scripts/          # Python scripts for ingestion
data/
  raw/            # Raw API responses
  clean/          # Cleaned datasets
docs/             # Documentation and notes
.env.example      # Template for environment variables
requirements.txt  # Python dependencies
.gitignore        # Ignore rules (env files, data folders, cache)
```


##  Setup Instructions

Follow the steps below to set up the environment.

1. Verify Python version
```bash
python --version
```

3. Clone the repository
```bash
git clone https://github.com/UBC-Live/Google-Places.git
cd Google-Places
```

5. Create a virtual environment
```bash
macOS / Linux

python3 -m venv .venv
source .venv/bin/activate
```


Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

6. Add your environment variables

```
Create a .env file in the project root (or copy .env.example):

GOOGLE_PLACES_API_KEY=your_key_here
```

##  Example Data Format

```
{
  "results": [
    {
      "place_id": "ChIJN1t_tDeuEmsRUsoyG83frY4",
      "name": "Starbucks",
      "formatted_address": "6133 University Blvd, Vancouver, BC",
      "geometry": {
        "location": {
          "lat": 49.2668,
          "lng": -123.2550
        }
      },
      "rating": 4.2,
      "user_ratings_total": 133,
      "business_status": "OPERATIONAL",
      "opening_hours": {
        "open_now": true
      },
      "types": [
        "cafe",
        "store",
        "point_of_interest",
        "food",
        "establishment"
      ]
    }
  ],
  "status": "OK"
}
```




##  🏗️ Data Flow

Ingestion scripts in `/scripts/` call the Google Places API.

Full API responses are saved in `/data/raw/` with timestamps.

Cleaning scripts transform and standardize the data.

Cleaned datasets are stored in `/data/clean/`.

Documentation (API notes, schema, etc.) is stored in `/docs/`.
