# algun ejemplo de diccionario (dict)
persona = {"nombre": "Luis", "edad": 50, "residencia": "Colombia"}

persona = {
            "nombre": "Luis", 
            "edad": 50, 
            "residencia": "Colombia"
            }

cliente = dict(
                nombre="luis",
                telefono="123456789"
                )

# imprimir un elemento del diccionario
print(cliente["nombre"])
print(cliente.get("telefono"))

paciente = {"nombre": "Luis Molero", "especie": "perritu", "edad": 5, "vacunado": True}

# Uso del método .keys()
print("\nClaves registradas en el diccionario\n")
for clave in paciente.keys():
    print(f"Claves disponibles {clave}")

print("\nValores disponibles en el diccionario\n")
for valor in paciente.values():
    print(f"Valores disponibles {valor}")
    
print("\nRegistro completo de pacientes registrados\n")
for clave, valor in paciente.items():
    print(f"Clave: {clave} - Valor: {valor}")

# Actualizar un registro de diccionario
print("\nActualización del registro del pacientes\n")
paciente.update({"especie": "Canino", "edad": 5, "vacunado": False})
for clave, valor in paciente.items():
    print(f"Clave: {clave} - Valor: {valor}")

# Eliminar registro PERO ANTES LO MOSTRAMOS
dato_eliminado = paciente.pop("vacunado", False)
print(dato_eliminado)
print(paciente)

