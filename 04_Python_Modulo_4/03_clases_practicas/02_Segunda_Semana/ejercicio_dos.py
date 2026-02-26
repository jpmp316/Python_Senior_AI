import csv
from pathlib import Path

FILE_PATH = Path("Inventario_dos.csv")

def create_inventory_file() -> None:
    fieldnames = ["id", "nombre", "precio", "stock"]
    
    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {
                "id":1, 
                "nombre": "Mouse", 
                "precio": 40, 
                "stock": 10
            }
        )
        writer.writerow(
            {
                "id":2,
                "nombre": "Teclado",
                "precio": 30,
                "stock": 5
            }
        )
        writer.writerow(
            {
                "id": 3,
                "nombre": "Monitor",
                "precio": 250,
                "stock": 3
            }
        )
        
def read_inventory() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe")
        return
    
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n*** INVENTARIO ***\n")
        for row in reader:
            print(row)
    
def read_inventory_formatted() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe")
        return
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n *** INVENTARIO CON FORMATO DE SALIDA ***")
        for row in reader:
            print(
                f"ID: {row['id']} | "
                f"Producto: {row['nombre']} | "
                f"Precio: {row['precio']} | "
                f"Stock: {row['stock']}"
            )

def main() -> None:
    create_inventory_file()
    read_inventory()
    read_inventory_formatted()

if __name__ == "__main__":
    main()

