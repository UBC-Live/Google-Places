## Overview
This document explains how to access **Google Places API (Web Service)** for the UBC LIVE real-time ingestion system. It includes authentication details, endpoints used, example requests, example reponses, rate limits, and important notes for the team.

## 1. Official Documentation Link
Google Places API (Nearby Search):
https://developers.google.com/maps/documentation/places/web-service/search-nearby

This is the endpoint used for retrieving real-time place information.

Google

## 2. Authentication
The API uses a Google Maps Platform API key.
1. Enable **Places API** in Google Cloud Console
2. Create an API key with Places API enabled
3. Save the key in the project ```.env``` file:
   
   ```GOOGLE_PLACES_API_KEY="YOUR_API_KEY_HERE"```
   
   note: Do **NOT** commit ```.env``` to GitHub.

## 3. Endpoint Used
**Nearby Search API (Web Service)**

Returns a list of places near a geographic coordinate.

Base URL: https://maps.googleapis.com/maps/api/place/nearbysearch/json

**Required Parameters**
| Parameter | Description |
| --------- | ----------- |
| ```location``` | Latitude,longitude (e.g., ```49.2606,-123.2460``` for UBC) |
| ```radius``` | Search radius in meters (e.g., ```500```) |
| ```type``` | Type of place (e.g., ```cafe```, ```restaurant```) |
| ```key``` | API key stored in ```.env``` |

**Optional Parameters**
| Parameter | Description |
| --------- | ----------- |
| ```keyword``` | Filter by keyword (e.g., “Starbucks”) |
| ```name``` | Filter by name |


