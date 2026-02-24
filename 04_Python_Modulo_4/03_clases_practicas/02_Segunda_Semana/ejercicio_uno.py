import csv
from pathlib import Path

FILE_PATH = Path("inventario.csv")

def create_inventory_file() -> None:
    with FILE_PATH.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file) # función tradicional para escribir en un archivo
        
        writer.writerow(["id", "nombre", "precio", "stock"])
        
        writer.writerow([1, "Mouse", 40, 10])
        writer.writerow([2, "Teclado", 30, 5])
        writer.writerow([3, "Monitor", 250, 3])

def read_inventory() -> None:
    if not FILE_PATH.exists():
        print("El archivo no existe. ")
        return
    
    with FILE_PATH.open("r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("\n*** INVENTARIO ***\n")
        
        for row in reader:
            print(row)

