# Google Places API — Data Privacy Requirements

This project uses the Google Places API. To comply with Google’s data privacy standards, the following rules must be followed:

## 1. User Data Privacy
- Do not collect or store personal data unless strictly necessary for functionality.
- Inform users if their location or personal information is being used.
- Include a privacy policy if this project becomes a user-facing application.

## 2. Location Data
- Only request the minimum location information required.
- Do not store precise user location data without consent.
- Provide users with an option to disable location usage if applicable.

## 3. Storage of Google Places Data
Google Places imposes restrictions on storing or reusing their data:

Allowed:
- Storing *Place IDs* long-term.
- Caching API results temporarily (for performance).

Not allowed:
- Storing full Google Places data permanently (names, coordinates, ratings, etc.).
- Building your own POI database from Google data.
- Sharing Google Places data with third parties.

## 4. Compliance Responsibilities
All contributors must follow:
- Google Maps Platform Terms of Service  
- Google Places API Policies  
- Local data protection laws (e.g., PIPEDA, GDPR if applicable)

Compliance is mandatory for using the API in this project.
