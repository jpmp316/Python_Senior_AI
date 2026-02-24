from service.service_inventory import InventoryService
from repository.repository_inventory import ProductRepository
from models.model_inventory import Product

def main():

    service = InventoryService(ProductRepository("data/data_inventory.csv"))

    while True:
        print("\n1. Agregar producto")
        print("2. Listar productos")
        print("3. Salir")

        op = input("Seleccione: ")

        if op == "1":
            try:
                p = Product(
                    int(input("ID: ")),
                    input("Nombre: "),
                    float(input("Precio: ")),
                    int(input("Stock: "))
                )
                service.add_product(p)
                print("Guardado")
            except Exception as e:
                print("Error:", e)

        elif op == "2":
            for p in service.list_products():
                print(p)

        elif op == "3":
            break

if __name__ == "__main__":
    main()
