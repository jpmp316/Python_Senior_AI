from repository.repository_inventory import ProductRepository
from models.model_inventory import Product

class InventoryService:

    def __init__(self, repo: ProductRepository) -> None:
        self._repo = repo

    def add_product(self, product: Product) -> None:
        products = self._repo.get_all()

        if any(p.id == product.id for p in products):
            raise ValueError("Producto duplicado")

        products.append(product)
        self._repo.save_all(products)

    def list_products(self) -> list[Product]:
        return self._repo.get_all()
