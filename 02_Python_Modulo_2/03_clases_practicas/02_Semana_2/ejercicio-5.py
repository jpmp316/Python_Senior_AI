from abc import ABC, abstractmethod

# interfaz para generar reportes
class GenerarReporte(ABC):
    
    @abstractmethod
    def generar_reporte(self) -> None:
        pass

class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto
    
    @abstractmethod
    def procesar_pago(self) -> None:
        pass

class PagoCriptomoneda(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"Procesando el pago con criptomonedas por ${self.monto:,.2f}")

class PagoBancario(SistemaPago, GenerarReporte):
    
    def procesar_pago(self) -> None:
        print(f"Procesando transferencia bancaria por un monto de ${self.monto:,.2f}")
        
    def generar_reporte(self) -> None:
        print("Reporte: Pago realizado mediante sistema bancario")

def ejecutar_pago(pago:SistemaPago) -> None:
    pago.procesar_pago()

def main() -> None:
    pago1 = PagoBancario(123456.65487)
    pago2 = PagoCriptomoneda(987654.321654897)
    
    ejecutar_pago(pago1)
    pago1.generar_reporte()
    
    ejecutar_pago(pago2)

if __name__ == "__main__":
    main()