# Usar set para validar si un usuario tiene acceso a un sistema.

from typing import Set, List, Tuple

def _obtener_usuarios_con_acceso(
    usuarios_autorizados: Set[str],
    usuarios_intentando: Set[str]
)-> Set[str]:
    return {u for u in usuarios_intentando if u in usuarios_autorizados}
    
def _obtener_usuarios_sin_acceso(
    usuarios_autorizados: Set[str],
    usuarios_intentando: Set[str]
) -> Set[str]:
    return {u for u in usuarios_intentando if u not in usuarios_autorizados}

def validar_acceso(
    usuarios_autorizados: Set[str],
    usuarios_intentando: Set[str]
) -> Tuple[Set[str], Set[str]]:
    
    autorizados = set(usuarios_autorizados)
    intentando = set(usuarios_intentando)
    
    acceso = _obtener_usuarios_con_acceso(autorizados, intentando)
    no_acceso = _obtener_usuarios_sin_acceso(autorizados, intentando)
    
    return acceso, no_acceso

def main() -> None:
    autorizados = {"Alexis", "Julian", "Pablo"}
    intentando = {"Ignacio", "Jerónimo", "Anobis", "Julian", "Diego", "Pablo"}
    
    acceso, no_acceso = validar_acceso(autorizados, intentando)
    
    print("Con acceso: ", acceso)
    print("Sin acceso: ", no_acceso)
    
if __name__ == "__main__":
    main()
