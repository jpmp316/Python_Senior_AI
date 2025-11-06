# Función sin parametros ni retorno
def saludar():
    print("Holaaaaaa parce... (pana)")

saludar()

def saludo():
    return "Holaaaaaa parce... (pana)"

print(saludo())

# Funciones con parametros
def saludotres(nombre):
    print(f"Como estas {nombre}")

saludotres("Luis Guillermo")
saludotres(3)

def suma(numeroUno: int, numeroDos: int) -> int:
    resultado = numeroUno + numeroDos
    print(f"El resultado de la suma de {numeroUno} + {numeroDos} es: {resultado}")

suma(5, 5)

# funciones con parametros con valores por defecto
def presentar_estudiante(nombre: str, carrera: str ="Ingeniería") -> str:
    print(f"Estudiante: {nombre} | Carrera: {carrera}")

presentar_estudiante("Camilo")
presentar_estudiante("Maryam", "Medicina")

# Funciones con efecto colateral
estudiantes =[]

def agregar_estudiante(nombre: str):
    estudiantes.append(nombre)
    
agregar_estudiante("Gilberto")
agregar_estudiante("Cristhian")
agregar_estudiante("Juan")
agregar_estudiante("Kevin")
agregar_estudiante("Melany")
agregar_estudiante("Oliver")
agregar_estudiante("Rigel")
print(estudiantes)

