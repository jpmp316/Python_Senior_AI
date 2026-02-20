def validate_title(title: str) -> str:
    title = title.strip()
    
    if not title:
        raise ValueError("La tarea no puede estar vacía")
    
    if len(title) > 60:
        raise ValueError(" El nombre de la tarea es excede el limite de caracteres")
    
    if "|" in title:
        raise ValueError("Uso de caracter invalido (barra vertical)")

    return title
