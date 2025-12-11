from datetime import datetime

class Accion:
    
    def __init__(self, descripcion: str) -> None:
        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción de la acción no puede estar vácia")
        self._descripcion = descripcion.strip()
        self._fecha_hora = datetime.now()
        
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def fecha_hora(self) -> datetime:
        return self._fecha_hora
    
    def __str__(self) -> str:
        fecha_str = self._fecha_hora.strftime("%y-%m-%d %H:%M:%S")
        return (f"[{fecha_str}] {self.descripcion}")
    
        