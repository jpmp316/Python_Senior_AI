import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from app.comisiones import calcular_comision


def test_ventas_negativas_lanzan_excepcion():
    #Arrange:
    ventas = -100
    
    # Act y Assert
    with pytest.raises(ValueError):
        calcular_comision(ventas)

def test_ventas_sin_comision():
    # Arrange
    ventas = 800
    
    # Act
    resultado = calcular_comision(ventas)
    
    # Assert
    assert resultado == 0

def test_comision_media():
    # Arrange
    ventas = 2000
    
    # Act
    resultado = calcular_comision(ventas)
    
    # Assert
    assert resultado == ventas * 0.05

def test_comision_alta():
    # arrange
    ventas = 6000
    
    # Act
    resultado = calcular_comision(ventas)
    
    # Assert
    assert resultado == ventas * 0.10