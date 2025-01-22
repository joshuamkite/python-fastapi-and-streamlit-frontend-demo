from fastapi.testclient import TestClient
from app import app  # Import app from app.py

client = TestClient(app)


def test_read_products():
    response = client.get("/products")
    assert response.status_code == 200
    products = response.json()
    assert len(products) == 3
    assert products[0]["name"] == "apple"


def test_read_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "apple",
        "price": 0.5,
        "stock_quantity": 100
    }


def test_read_product_not_found():
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_create_product():
    new_product = {
        "id": 4,
        "name": "dragonfruit",
        "price": 2.5,
        "stock_quantity": 30
    }
    response = client.post("/products", json=new_product)
    assert response.status_code == 200
    assert response.json() == new_product


def test_create_product_duplicate_id():
    duplicate_product = {
        "id": 1,  # Already exists
        "name": "new_apple",
        "price": 1.0,
        "stock_quantity": 50
    }
    response = client.post("/products", json=duplicate_product)
    assert response.status_code == 409
    assert response.json()["detail"] == "Product ID already in use"


def test_create_product_duplicate_name():
    duplicate_product = {
        "id": 10,
        "name": "apple",  # Already exists
        "price": 1.0,
        "stock_quantity": 50
    }
    response = client.post("/products", json=duplicate_product)
    assert response.status_code == 409
    assert response.json()["detail"] == "Product name already in use"


def test_update_product():
    updated_product = {
        "id": 1,
        "name": "apple",
        "price": 0.75,
        "stock_quantity": 90
    }
    response = client.put("/products/1", json=updated_product)
    assert response.status_code == 200
    assert response.json() == updated_product


def test_update_product_id_mismatch():
    product = {
        "id": 2,  # Mismatched with URL
        "name": "apple",
        "price": 0.75,
        "stock_quantity": 90
    }
    response = client.put("/products/1", json=product)
    assert response.status_code == 400
    assert response.json()["detail"] == "ID mismatch"


def test_update_product_not_found():
    product = {
        "id": 999,
        "name": "not_found",
        "price": 1.0,
        "stock_quantity": 50
    }
    response = client.put("/products/999", json=product)
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_delete_product():
    response = client.delete("/products/2")
    assert response.status_code == 200
    # Verify product is deleted
    get_response = client.get("/products/2")
    assert get_response.status_code == 404


def test_delete_product_not_found():
    response = client.delete("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"
