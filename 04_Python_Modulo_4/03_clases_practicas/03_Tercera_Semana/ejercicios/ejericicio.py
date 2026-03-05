try:
    edad = int(input("Ingrese su edad:"))
except ValueError:
    print("Debe ingresar un número")


try:
    edad = int(input("Ingrese su edad:"))
except ValueError:
    print("Debe ingresar un número")
except TypeError:
    print("Tipo de dato invalido")
except Exception as e:
    print(f" Ocurrió un error inesperado: {e}")


try:
    edad = int(input("Ingrese su edad:"))
except ValueError:
    print("Debe ingresar un número entero")
else:
    print("La ejecución dio un resultado positivo (Else)")
finally:
    print("La ejecución finalizó")
