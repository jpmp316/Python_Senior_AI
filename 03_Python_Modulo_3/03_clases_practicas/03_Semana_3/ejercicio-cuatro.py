"""
Enunciado del ejercicio:

Una empresa tiene dos tiendas que venden productos distintos y, en algunos casos, coinciden en el inventario.
Escriba un programa en Python que:

1. Reciba como conjuntos los productos disponibles en la "Tienda A" y en la tienda "Tienda B".
2. Calcule y muestre:

   * "La unión" de productos: todos los productos disponibles en ambas tiendas, sin duplicados.
   * "La intersección" de productos: los productos que ambas tiendas tienen en común.
   * "La diferencia" de productos: los productos que están en la Tienda A pero no en la Tienda B.

"""

def operaciones_productos(tienda_a: set, tienda_b: set):
    union = tienda_a | tienda_b
    interseccion= tienda_a & tienda_b
    diferencia = tienda_a - tienda_b
    return union, interseccion, diferencia

def main():
    tienda_a = {"Laptop", "Mouse", "Teclado"}
    tienda_b = {"Mouse", "Pantalla", "Laptop"}
    
    union, interseccion, diferencia = operaciones_productos(tienda_a, tienda_b)
    
    print("Unión: ", union) # Laptop, Mouse, Teclado, Pantalla
    print("Intersección: ", interseccion) # Mouse, Laptop
    print("Diferencia: ", diferencia) # Teclado
    
if __name__ == "__main__":
    main()
