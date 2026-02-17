from calculadora import promedio

def test_promedio():
    # Arrange
    data = [1, 2, 3, 4, 5]
    
    # Act
    resultado = promedio(data)
    
    # Assert
    assert resultado == 3.0
def test_promedio_vacio():
    # Arrange
    data = []
    
    # Act
    resultado = promedio(data)
    
    # Assert
    assert resultado == 0.0
    
def test_promedio_con_error():
    # Arrange
    data = [1, 2, 'tres', 4, 5]
    
    # Act
    resultado = promedio(data)
    
    # Assert
    assert resultado == 3.0

def test_con_elemento_vacio():
    # Arrange
    data = [1, 2, None, 4, 5]
    
    # Act
    resultado = promedio(data)
    
    # Assert
    assert resultado == 3.0