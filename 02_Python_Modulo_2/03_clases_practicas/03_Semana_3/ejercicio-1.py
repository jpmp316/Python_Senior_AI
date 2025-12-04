# Sistema de restaurante - POO Avanzada

from abc import ABC, abstractmethod
from typing import List

# Superclase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_valor: str) -> None:
        if isinstance(nuevo_valor, str) and nuevo_valor.strip():
            self._nombre = nuevo_valor
        else:
            raise ValueError("El nombre debe ser una cadena de texto válida")
        
    @abstractmethod
    def presentar(self) -> None:
        pass

# Subclases

class Cliente(Persona):
    def presentar(self) -> None:
        print(f"El cliente {self.nombre} ha llegado al restaurante")

# subclase
class Empleado(Persona):
    @abstractmethod
    def trabajar(self) -> None:
        pass
    
class Mesero(Empleado):
    def presentar(self) -> None:
        print(f"El mesero {self.nombre} se encuentra listo para atender")
    
class Chef(Empleado):
    def presentar(self) -> None:
        print(f"El Chef {self.nombre} se encuentra en la cocina")
    
    def trabajar(self) -> None:
        print(f" El Chef {self.nombre} esta preparando un plato")

# Composición
class Cocina:
    

    