# Google Places API — Licensing Requirements

This document summarizes the licensing and usage restrictions related to the Google Places API.

## 1. Attribution Requirement
Whenever Google Places data is displayed, the application must include:
> "Powered by Google"

This attribution must be visible wherever place information is shown.

## 2. Permitted Uses
- You may request place details, photos, autocomplete results, and geodata.
- You may store:
  - Place IDs permanently
  - Short-term cached responses

## 3. Prohibited Uses
Google does NOT allow:
- Permanent storage of place details (name, rating, address, coordinates)
- Exporting Places data outside your application
- Sharing raw Google Places data with third parties
- Using Google data to create your own location/places database
- Scraping or bulk-extracting Google data

## 4. API Key Requirements
- A valid, non-exposed API key must be used.
- Keys must be secured in environment variables (e.g., `.env`).
- Keys must not be committed to Git or shared publicly.

## 5. Legal Compliance
This project must follow:
- Google Maps Platform Terms of Service  
- Google Places API Terms of Service  

Non-compliance may result in API key suspension.
