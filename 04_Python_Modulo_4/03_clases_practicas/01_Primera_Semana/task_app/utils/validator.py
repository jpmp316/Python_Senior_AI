def validate_title(title: str) -> str:
    title = title.strip()
    
    if not title:
        raise ValueError("La tarea no puede estar vacía")
    
    if len(title) > 60:
        raise ValueError(" El nombre de la tarea es excede el limite de caracteres")
    
    if "|" in title:
        raise ValueError("Uso de caracter invalido (barra vertical)")

    return title

def validate_index(index: int, size: int) -> int:
    if size == 0:
        raise ValueError("No hay tareas registradas")
    if index < 1:
        raise ValueError("El indice de la tareaa modificar de ser superior a 0")
    if index > size:
        raise ValueError("El indice de latarea modificar debe estar dentro del rago de registros")
    
    return index - 1

