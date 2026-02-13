def calcular_recargo(siniestros, es_premium):
    if siniestros <= 2:
        return 0
    if es_premium:
        return 0.15
    return 0.30

def test_cliente_sin_siniestros():
    # AAA = Arrange-Act-Assert
    # Arrange
    siniestros = 0
    es_premium = False
    
    # Act
    resultado = calcular_recargo(siniestros, es_premium)
    
    #Assert
    assert resultado == 0

def test_cliente_riesgoso():
    # Arrange
    siniestros = 3
    es_premium = False
    
    # Act
    resultado = calcular_recargo(siniestros, es_premium)
    
    #Assert
    assert resultado == 0.30

def test_cliente_premium_limita_recargo():
    # Arrange
    siniestros = 5
    es_premium = True
    
    # Act
    resultado = calcular_recargo(siniestros, es_premium)
    
    #Assert
    assert resultado == 0.15

def _ejecutar_pruebas_basicas():
    test_cliente_sin_siniestros()
    test_cliente_riesgoso()
    test_cliente_premium_limita_recargo()

def _demo():
    ejemplos = [
        (0, False),
        (3, False),
        (5, True),
    ]
    
    for siniestros, es_premium in ejemplos:
        recargo = calcular_recargo(siniestros, es_premium)
        
        print(f"Siniestros={siniestros}, Premium={es_premium} -> Recargo={recargo:.2f}")

if __name__ == "__main__":
    _ejecutar_pruebas_basicas()
    _demo()