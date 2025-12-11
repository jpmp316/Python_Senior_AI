from abc import ABC, abstractmethod


class Rol(ABC):

    @abstractmethod
    def aplicar_regla(self, monto: float) -> float:
        pass

    @abstractmethod
    def descripcion(self) -> str:
        pass


class RolRegular(Rol):
    def aplicar_regla(self, monto: float) -> float:
        return monto

    def descripcion(self) -> str:
        return "Cliente Regular"


class RolVIP(Rol):
    def aplicar_regla(self, monto: float) -> float:
        return round(monto * 0.90, 2)

    def descripcion(self) -> str:
        return "Cliente VIP"


class RolEmpresarial(Rol):
    def aplicar_regla(self, monto: float) -> float:
        return monto

    def descripcion(self) -> str:
        return "Cliente Empresarial"
