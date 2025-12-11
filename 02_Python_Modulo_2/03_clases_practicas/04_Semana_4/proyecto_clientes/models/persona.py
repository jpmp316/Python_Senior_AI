from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(
        self, 
        nombre: str, 
        documento: str
        ) -> None:
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre.strip().title()
        else:
            raise ValueError("El nombre debe ser un texto no vacío.")
        
        if isinstance(documento, str) and documento.strip():
            self._documento = documento.strip()
        else:
            raise ValueError("El documento/identificación no puede estar vacío.")

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip().title()
        else:
            raise ValueError("El nombre debe ser un texto no vacío.")

    @property
    def documento(self) -> str:
        return self._documento

    @documento.setter
    def documento(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._documento = valor.strip()
        else:
            raise ValueError("El documento/identificación no puede estar vacío.")

    @abstractmethod
    def presentar(self) -> None:
        pass

