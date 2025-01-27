# Streamlit Frontend

A Streamlit-based frontend for accessing the accompanying FastAPI API based around managing product inventory.

## Features
- View product list
- Add new products
- Error handling for duplicate IDs/names
- Formatted table display

## Local Development
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
streamlit run app.py
```

## Docker
Build and run:
```bash
docker build -t inventory-frontend .
docker run -p 8501:8501 inventory-frontend
```

## Environment Variables
- `API_URL`: Backend API URL (default: http://localhost:8000)

## Access
Open http://localhost:8501 in your browser