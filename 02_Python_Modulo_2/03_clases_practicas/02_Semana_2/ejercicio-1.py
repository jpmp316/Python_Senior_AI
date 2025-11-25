"""
# Herencia 
class Vehiculo:
    def mover(self):
        print("El vehiculo se está moviendo")
    
class Carro(Vehiculo):
    pass

def main():
    vehiculo1 = Vehiculo()
    carro1 = Carro()
    
    print("Vehiculo")
    vehiculo1.mover()
    
    print("Carro que hereda de la superclase Vehiculo")
    carro1.mover()

if __name__ == "__main__":
    main()


# Sobre escritura

class Vehiculo():
    def mover(self):
        print("El vehiculo se está moviendo")
        
class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle")
    
def main():
    vehiculo2 = Vehiculo()
    carro2 = Carro()
    
    print("Vehiculo")
    vehiculo2.mover()
    
    print("El carro sobre escribio el método (def) mover ya que se movimiento es a traves de ruedas")
    carro2.mover()
    
if __name__ == "__main__":
    main()
    

# Polimorfismo
class Vehiculo():
    def mover(self):
        print("El vehiculo se está moviendo")

class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle")

class Avion(Vehiculo):
    def mover(self):
        print("El avión esta volando sobre la ciudad")
        
def main():
    vehiculo3 = Vehiculo()
    carro3 = Carro()
    avion3 = Avion()
    
    print("Vehiculo")
    vehiculo3.mover()
    
    print("Carro")
    carro3.mover()
    
    print("AVión")
    avion3.mover()

if __name__ == "__main__":
    main()


# super()
class Padre():
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
        
class Hijo(Padre):
    def __init__(self, mensaje, nombre) -> None:
        super().__init__(mensaje)
        self.nombre = nombre
        
def main():
    objeto1 = Hijo("Hola desde la clase Hijo", "Luis Guillermo")
    print(objeto1.mensaje)
    print(objeto1.nombre)
    
if __name__ == "__main__":
    main()
    


# ejercicio real

class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")

def main():
    gerente = Gerente("Luis Molero", 9000000000, "TIC")
    gerente.mostrar_informacion()

if __name__ == "__main__":
    main()
    


# ejemplo con polimorfismo

class Empleado():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    
    def trabajar(self):
        print(f"{self.nombre} esta realizando una tarea general")
        
class Gerente(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta coordinando a su equipo de trabajo")

class Desarrollador(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta desarrollando software")

def main():
    empleados = [
        Gerente("Maryam"),
        Desarrollador("Juan Esteban"),
        Empleado("Kevin")
    ]
    
    print("POLIMORFISMO")
    for empleado in empleados:
        empleado.trabajar()

if __name__ == "__main__":
    main()
    
"""

# Desarrolle una super aplicaciónpara una Veterinaria

# Superclase:
# Animales
# Subclases:
# Perritos
# Gaticos
