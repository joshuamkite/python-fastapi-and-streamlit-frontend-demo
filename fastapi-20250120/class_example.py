class Product:
    """class Product"""

    def __init__(self, id: int, name: str, price: float, stock_quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity


apple = Product(
    id=1,
    name="apple",
    price=0.5,
    stock_quantity=100
)

banana = Product(
    id=2,
    name="banana",
    price=0.6,
    stock_quantity=50
)

print(f"debug: apples cost {apple.price} each")
print(f"debug: bananas cost {banana.price} each")
