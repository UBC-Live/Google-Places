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
