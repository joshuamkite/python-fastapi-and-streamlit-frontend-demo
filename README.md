# Product Inventory System

A containerized product inventory system with FastAPI backend and Streamlit frontend.

## Architecture
- Backend: FastAPI REST API
- Frontend: Streamlit web interface
- Docker containers for both services

## Quick Start
1. Clone repository
2. Run with Docker Compose:
```bash
docker compose up --build
```

3. Access:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs

## Directory Structure
```
.
├── backend-fastapi/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── frontend-streamlit/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── compose.yaml
```

## Development
See individual README files in frontend and backend directories for local development instructions.