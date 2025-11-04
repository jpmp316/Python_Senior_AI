contador = 1

while contador <= 5:
    print("contador", contador)
    contador += 1 # Incrementando la variable en la unidad
    
print("Fin del ciclo")

# Permita solicitar una palabra por teclado y escribir "salir" para salir de la app

palabra = ""

while palabra != "salir":
    palabra = input("Por favor, ingrese una palabra (Salir... para finalizar)")
    print(f"Escribiste la palabra => {palabra}")

print("Programa finalizado...")


# Menú por consola

opcion = ""

print("********* Menú por consola **********")
print("Opción 1: Saludar")
print("Opción 2: Mensaje")
print("Opción 3: Salir")

while True:
    opcion = input("Ingrese una opción (1-3): ")
    
    if opcion == "1":
        print("Hola, como estas?")
    elif opcion == "2":
        print("La verdadera generosidad para con el futuro consiste en entregarlo todo al presente (Albert Camus)")
    elif opcion == "3":
        print("Saliendo de la aplicación")
        break

# Suma acumulada de números: Se solicitan números al usuario y acumula su suma hasta que escriba 0.

suma = 0
numero = int(input("Ingrese un número (0 para salir)"))

"""
    != diferente a
"""
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para salir)"))

print(f"La suma total es => {suma}")


# Validar entrada positiva: Solicita un número positivo, si el usuario ingresa un valor negativo, repite la solicitud

numero = int(input("Ingrese un número positivo: "))

while numero < 0:
    print("ERROR: Debes ingresar un número positivo")
    numero = int(input("Por favor, te solicito amablemente ingresar un número positivo: "))
    
print(f"El número ingresado es: {numero}")


# For => Se utiliza para recorrer una secuencia como: lista, rangos de números o cadenas de caracteres

# Quiero hacer un ciclo For para que me imprima los números del 1 al 6

for numero in range (1, 7): # Se imprimiran los números de 1 al 6
    print(f"El número a imprimir es  {numero}")

# Ahora, quiero imprimir una lista (estructura de datos) de elementos

productos = ["Pan", "Huevo", "Harina", "Leche", "Queso"]

for producto in productos:
    print(f"El producto es => {producto}")

# El uso del "break" y el "continue" dentro del ciclo "For"
# break

for numero in range (1, 7): # Se imprime hasta el número 3 por el uso del BREAK
    if numero == 4:
        print("Se interrumpio el ciclo For para excluir numeros a partir del 4")
        break
    print(f"El número a imprimir es  {numero}")
    

for numero in range (1, 7): # Se salta la impresión del número 4 por el uso del CONTINUE
    if numero == 4:
        print("\n\n Por el uso de la PALABRA RESERVADA CONTINUE se salta la impresión del número 4\n\n")
        continue
    print(f"El número a imprimir es  {numero}")


for numero in range (1, 7, 2): # Se imprime los números desde el 1, con incremento de 2 hasta el 6
    print(f"El número a imprimir es  {numero}")


# Imprimir una cadena de caracteres (string => str) uno por uno. Ejemplo de caracteres: ú, R, s, !, "5", &...

cadena = input("Por favor, ingrese una cadena de caracteres: ")

for caracter in cadena:
    print(caracter)
    
    
    
# Desarrolle una app en python que permita sumar los números de 1 al 100
# Desarrolle una app en python que permita calcular el cuadrado de los números de 1 al 5
# Desarrolle una app en python que permita mostrar solo las vocales de una palabra
# Desarrolle una app en python que permita imprimir la tabla de multiplicar de un número ingresado por teclado
