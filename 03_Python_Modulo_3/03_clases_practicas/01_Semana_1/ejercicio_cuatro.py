colores = ("amarillo", "azul", "rojo")
print(colores[2]) #rojo
print(colores[1]) #azul

# tupla con valores diferentes
personal = ("Juan Pablo", 22, True)

print(personal[0]) # Juan Pablo
print(personal[2]) # True

for color in colores:
    print(color)

# Desempaquetado de Tuplas

nombre, edad, edo_civil = personal
print(nombre)
print(edad)
print(edo_civil)

# Tratando de modificar una Tupla
persona = ("Juan Pablo", 22, True)

persona[1] = 29 # error

persona = ("Juan Pablo", 29, True)

