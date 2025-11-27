from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    
class Circulo(Figura):
    
    def __init__(self, radio: float):
        self.radio = radio
    
    def calcular_area(self):
        area = 3.1416 * (self.radio ** 2)
        return area
    
    def calcular_radio(self):
        pass
    
    def calcular_perimetro(self):
        pass

def main():
    figura1 = Circulo(5.0)
    print(f"El área del círculo es: {figura1.calcular_area():,.2f}")

if __name__ == "__main__":
    main()
    
"""
Desarrolle una app que cree una clase abstracta "Estudiante" y al menos 3 subclases y como minmimo 2 comportamientos/funciones/métodos/definiciones.
"""