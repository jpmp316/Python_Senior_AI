# PRÁCTICA EMPRESARIAL: Registro de empleados

# Caso real: Registro de contratos en RRHH

# El departamento de RRHH almacena un registro histórico de contratos de empleados (nombre, cargo y salario). Estos datos no deben ser modificados una vez firmados, por lo que se debe usar una tupla por empleado.

from typing import Tuple, List
from dataclasses import dataclass

# Excepciones de dominio

class ListaEmpleadosVaciaError(Exception):
    pass

# Validación

def _validar_datos_empleado(nombre: str, cargo: str, salario: float) -> None:
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError("El nombre no debe ser un texto vacío.")
    
    if not isinstance(cargo, str) or not cargo.strip():
        raise ValueError("El argo no debe ser un texto vacío.")
    
    if not isinstance(salario, (int, float)):
        raise ValueError("El salario debe ser un valor numérico")
    
    if salario <= 0:
        raise ValueError("El salario debe ser mayor a cero")

# Services - Servicios - Lógica del negocio

def registrar_empleado(nombre: str, cargo: str, salario: float) -> Tuple[str, str, float]:
    _validar_datos_empleado(nombre, cargo, salario)
    
    return (
        nombre.strip().title(),
        cargo.strip().title(),
        float(salario)
    )

# Result Pattern ó Patrón de Diseño "Resultado"

@dataclass
class ResultadoRegistro:
    empleados: List[Tuple[str, str, float]]
    errores: List[str]
    
def registrar_empleados(datos: List[Tuple[str, str, float]]) -> ResultadoRegistro:
    empleados_registrados: List[Tuple[str, str, float]] = []
    errores: List[str] = []
    
    for nombre, cargo, salario in datos:
        try: 
            empleados_registrados.append(registrar_empleado(nombre, cargo, salario))
        except (ValueError, TypeError) as error:
            errores.append(str(error))
            
    return ResultadoRegistro(
        empleados=empleados_registrados,
        errores=errores
    )

# Presentación

def mostrar_empleados(empleados: List[Tuple[str, str, float]]) -> None:
    if not empleados:
        raise ListaEmpleadosVaciaError("No existen registros para mostrar")
    
    print("Registro histórico de contratos de empleados")
    for indice, (nombre, cargo, salario) in enumerate(empleados, start=1):
        print(f"{indice}. {nombre} - {cargo} - ${salario:,.2f}")

def main() -> None:
    datos_prueba = [
        ("Ana García", "Ingeniera de Software", 8500),
        ("Luis Pérez", "Analista de Datos", 7200),
        ("Marta León", "Diseñadora UX", 6800)
    ]
    
    resultado = registrar_empleados(datos_prueba)
    
    try:
        mostrar_empleados(resultado.empleados)
    except ListaEmpleadosVaciaError as error:
        print(error)
        
    
    if resultado.errores:
        print(f"\nErrores capturados durante el proceso de registro por lote:")
        for error in resultado.errores:
            print(f"- {error}")

if __name__ == "__main__":
    main()
    
    