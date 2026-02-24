from models.model_inventory import Product
from utils.csv_manager import CSVManager
from utils.validator import validate_product

class ProductRepository:

    HEADERS = ["id", "name", "price", "stock"]

    def __init__(self, path: str) -> None:
        self._csv = CSVManager(path)

    def get_all(self) -> list[Product]:
        rows = self._csv.read_all()
        products = []

        for row in rows:
            clean = validate_product(row)
            products.append(Product(**clean))

        return products

    def save_all(self, products: list[Product]) -> None:
        rows = [product.__dict__ for product in products]
        self._csv.write_all(rows, self.HEADERS)
