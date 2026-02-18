"""
f = open("datos.txt", "r")
file1 = open("datos.txt", "w")
file2 = open("datos.txt", "a")
file3 = open("datos.txt", "r+")


with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

"""

with open("letras.txt", "w", encoding="utf-8") as f:
    f.write("A\n")
    f.write("B\n")

# Método de lectura .read()

with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Método .readline() para leer una linea a la vez

with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.readline())

# Método .readlines() imprime una lista de elementos contenidos en el archivo
with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.readlines())

# Convención
# Nombre|apellido|edad
# Luis|molero|50

# Arquitectura mínima p/manejo de archivos
# Presentación -> Interacción con el usuario
# Servicio -> modelo/reglas del negocio
# Repositorio -> accesso a los datos
# Infraestructura -> archivos físicos
# modelo/esquema -> datos

# Super software

"""
1. FileManager (infraestructura segura)
2. Modelo Task (serialización)
3. Repository (persistencia desacoplada)
4. Service (reglas de negocio + validación)
5. main (interfaz consola)
"""

# ToDo List


"""
    ## Estándares de calidad

| Norma                 | Aplicación                      |
| --------------------- | ------------------------------- |
| PEP8                  | nombres, longitud, imports      |
| DRY                   | no repetir lógica de archivo    |
| KISS                  | funciones pequeñas              |
| SRP                   | cada función hace una sola cosa |
| Fail Fast             | validar antes de guardar        |
| Defensive Programming | proteger el archivo             |
| Idempotencia          | leer no modifica estado         |
| Encapsulación         | no acceder directo al archivo   |
| Tipado fuerte         | typing obligatorio              |

"""

