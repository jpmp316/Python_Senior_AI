mi_set = set()
frutas = {"pera", "manzana", "banano"}

# conversión de lista a set
numeros = [1, 2, 3, 4]
conversion = set(numeros)
print(conversion)

frutas = {"pera", "manzana", "banano"}
frutas.add("uva")
print(frutas)

frutas.update(["kiwi", "mango"])
print(frutas)


frutas.discard("pera")
print(frutas)

frutas = sorted(frutas)
print(frutas)

#frutas.discard("pera") # si el elemento del set no existe, no da error al intentar borrarlo
#frutas.remove("pera") # Aquí si da error porque el elemento no existe

frutas.clear()

# Operaciones con set
# union
# intersección
# diferencia
# diferencia simétrica

a = {1, 2, 3}
b = {3, 4, 5}

# union
print(a | b) # {1, 2, 3, 4, 5}

#intersección
print(a & b) # {3}

# diferencia
print(a - b) # {1, 2}

print(a ^ b) # {1, 2, 4, 5}

# validación de elementos con set
usuarios = {"Maryan", "Pablo", "Ignacio"}
print("Maryan" in usuarios) #Tru
print("Luis" in usuarios) #False
