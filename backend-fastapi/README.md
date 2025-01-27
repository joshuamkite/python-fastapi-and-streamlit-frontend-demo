# FastAPI Backend

A demo FastAPI-based REST API based around managing product inventory.

## Features
- CRUD operations for products
- Input validation using Pydantic models
- Error handling for duplicate products
- Automated tests
- Health check endpoint

## API Endpoints
- `GET /products` - List all products
- `GET /products/{product_id}` - Get specific product
- `POST /products` - Add new product
- `PUT /products/{product_id}` - Update product
- `DELETE /products/{product_id}` - Delete product
- `GET /health` - Health check
- `GET /docs` - Get API documentation

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
uvicorn app:app --reload
```

## Testing
Run the test suite:
```bash
pytest test_app.py
```

### Test Coverage
The test suite covers:

1. Product Listing
- Verify GET /products returns all products
- Check correct initial product count
- Validate product data structure

2. Single Product Operations
- Get existing product by ID
- Handle requests for non-existent products
- Verify correct product details returned

3. Product Creation
- Add new product successfully
- Handle duplicate product ID errors
- Handle duplicate product name errors

4. Product Updates
- Update existing product
- Handle ID mismatches between URL and payload
- Handle updates to non-existent products

5. Product Deletion
- Delete existing product
- Verify product is actually deleted
- Handle deletion of non-existent products

## Docker
Build and run:
```bash
docker build -t inventory-backend .
docker run -p 8000:8000 inventory-backend
```

## API Documentation
Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Example API Usage

List all products:
```bash
curl http://localhost:8000/products
```

Get specific product:
```bash
curl http://localhost:8000/products/1
```

Add new product:
```bash
curl -X POST http://localhost:8000/products \
-H "Content-Type: application/json" \
-d '{"id": 4, "name": "dragonfruit", "price": 5, "stock_quantity": 12}'
```

Update product:
```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "apple", "price": 0.75, "stock_quantity": 200}' \
  http://localhost:8000/products/1
```

Delete product:
```bash
curl -X DELETE http://localhost:8000/products/1
```

## Access
- API: http://localhost:8000
- API documentation: http://localhost:8000/docs