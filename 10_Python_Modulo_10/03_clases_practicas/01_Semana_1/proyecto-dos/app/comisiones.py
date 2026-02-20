def calcular_comision(ventas: float) -> float:
    if ventas < 0:
        raise ValueError("Esta venta es invalida")
    if ventas < 1000:
        return 0
    if ventas < 5000:
        return ventas * 0.05
    return ventas * 0.1

# Testing para:
# 1. Ventas negativas
# 2. Ventas sin conmisiones
# 3. Ventas con comisiones medias
# 4. Ventas con comisiones altas


