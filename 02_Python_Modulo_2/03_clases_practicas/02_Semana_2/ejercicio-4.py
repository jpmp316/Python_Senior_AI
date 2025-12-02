from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None
        self.nombre = nombre
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre debe ser un texto nop vacio")
    
    @abstractmethod
    def trabajar(self) -> None:
        pass

class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta gestionando estrategias empresariales.")


class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta desarrollando una solución de software")

def ejecutar_tarea(empleado: Empleado) -> None:
    empleado.trabajar()

def main() -> None:
    empleado1 = Gerente("Luis Molero")
    empleado2 = Desarrollador("Carlos Palacio")
    
    ejecutar_tarea(empleado1)
    ejecutar_tarea(empleado2)
    
    empleado2.nombre = "Fernando Restrepo"
    print(f"El nombre nuevo del desarrollador es: {empleado2.nombre}")

if __name__ == "__main__":
    main()
    