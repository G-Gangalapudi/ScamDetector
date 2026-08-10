# Scam Intelligence

This repository now contains a basic FastAPI backend scaffold organized under the repository root.

## Structure

- backend/app/ - application package
- backend/tests/ - unit, integration, and API test folders
- backend/requirements.txt - Python dependencies
- docker-compose.yml - container setup for the backend

## Getting started

1. Install dependencies:
   - pip install -r backend/requirements.txt
2. Run the API locally:
   - uvicorn app.main:app --host 0.0.0.0 --port 8000
3. Or start with Docker:
   - docker compose up --build