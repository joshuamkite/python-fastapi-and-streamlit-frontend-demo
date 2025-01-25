I'll create a practical challenge that's representative of what you might encounter in a technical interview. Here's a scenario:

**Challenge: Product Inventory API**

Create a simple inventory management API that a retail store might use. The requirements are:

1. Create a FastAPI application with the following endpoints:
   - GET `/products` - List all products
   - GET `/products/{product_id}` - Get a specific product
   - POST `/products` - Add a new product
   - PUT `/products/{product_id}` - Update a product
   - DELETE `/products/{product_id}` - Delete a product

2. Each product should have:
   - id (integer)
   - name (string)
   - price (float)
   - stock_quantity (integer)

3. For this exercise, store the data in memory (no database needed)

Let's tackle this step by step. Would you like me to help you get started with the basic FastAPI setup and the first endpoint? We can then test it with curl, containerize it with Docker, and gradually build up the functionality.

This challenge will help you practice:
- REST API design
- Request/Response handling
- Data validation
- HTTP methods
- API testing with curl
- Docker containerization

Would you like to begin with the initial FastAPI setup?


-------------

 To run a FastAPI application, you need to use an ASGI server like Uvicorn. 

You need to:

1. First install uvicorn if you haven't already:
```bash
pip install uvicorn
```

2. Then run your application using uvicorn:
```bash
uvicorn app:app --reload
```

Here, the syntax is:
- `app:app` means "use the `app` variable from the `app.py` file"
- `--reload` enables auto-reload when code changes (useful during development)

The `--reload` flag is optional but helpful during development as it will automatically restart the server when you make changes to your code.

Once you run this command, your FastAPI application should start and you can access it at `http://localhost:8000`. You can also view the auto-generated API documentation at `http://localhost:8000/docs`.

## list all products

```bash
curl http://127.0.0.1:8000/products
```

## match and return on product.id

```bash
curl http://127.0.0.1:8000/products/1
```

## match and return on product.price


## Add a product

```bash
curl -X POST http://localhost:8000/add-product \
-H "Content-Type: application/json" \
-d '{"id": 4, "name": "dragonfruit", "price": 5, "stock_quantity": 12}'
```

## Update a product

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "apple", "price": 0.75, "stock_quantity": 200}' \
  http://localhost:8000/products/1
  ```

##  Delete a product
```bash
curl -X DELETE http://localhost:8000/products/1
```