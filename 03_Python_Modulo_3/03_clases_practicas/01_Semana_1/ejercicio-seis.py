#Slice

ventas_mensuales = [12000, 9800, 10200, 14500, 16000, 13200, 11000, 11700, 9800, 10500, 14000, 13800]

for venta in enumerate(ventas_mensuales, start=1):
    print(venta)

ventas_T2 = ventas_mensuales[3:6]

ventas_top = [v for v in ventas_mensuales if v > 13000]

print(f"Ventas del segundo trimestre: {ventas_T2}")
print(f"Ventas Top: {ventas_top}")

# Ejercicios:

"""
    Slicing: 
    Dada la lista:
    
    empleados = ["Ana", "Luis", "Carlos", "Marta", "Diana"]
    
    Hacer:
    
    1. Extrae los elementos desde “Luis” hasta “Marta” (inclusive).
    2. Extrae los elementos excluyendo el primero y el último.
    
    
    Slicing con pasos (step)
    Dada la lista:

    datos = [1, 2, 3, 4, 5, 6, 7, 8]
    
    Hacer:
    
    1. Obtén los elementos en posiciones pares.
    2. Obtén los elementos en posiciones impares.
"""