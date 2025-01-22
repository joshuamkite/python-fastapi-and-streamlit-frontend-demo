import fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    """class Product"""
    id: int
    name: str
    price: float
    stock_quantity: int


product_items = [
    {
        "id": 1,
        "name": "apple",
        "price": 0.5,
        "stock_quantity": 100
    },
    {
        "id": 2,
        "name": "banana",
        "price": 0.6,
        "stock_quantity": 50
    },
    {
        "id": 3,
        "name": "cherry",
        "price": 0.1,
        "stock_quantity": 1000
    }
]


products = [Product(**item) for item in product_items]

# Equivalent to:
# products = []

# for item in product_items:
#     products.append(Product(**item))

# The square brackets [ ] replace both the empty list creation and the append() method. They tell Python "create a new list containing everything that results from this expression."


@app.get("/products")
async def read_products() -> list[Product]:
    """list all products"""
    return products


@app.get("/products/{product_id}")
async def read_product_id(product_id: int) -> Product:
    """match and return on product.id"""
    for product in products:
        if product.id == product_id:
            return product
    raise fastapi.HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
async def post_product(product: Product) -> Product:
    """Add a new product"""
    for p in products:
        if p.id == product.id:
            raise fastapi.HTTPException(status_code=409, detail="Product ID already in use")
        if p.name == product.name:
            raise fastapi.HTTPException(status_code=409, detail="Product name already in use")
    products.append(product)
    return product


@app.put("/products/{product_id}")
async def put_product(product_id: int, product: Product) -> Product:
    """Update a product"""
    if product_id != product.id:
        raise fastapi.HTTPException(status_code=400, detail="ID mismatch")
    for i, p in enumerate(products):
        if p.id == product_id:
            products[i] = product
            return product
    raise fastapi.HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
async def del_product(product_id: int) -> Product:
    """Delete a product"""
    for i, p in enumerate(products):
        if p.id == product_id:
            return products.pop(i)
    raise fastapi.HTTPException(status_code=404, detail="Product not found")
