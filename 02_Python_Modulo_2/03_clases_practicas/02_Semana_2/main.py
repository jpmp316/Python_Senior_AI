from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._titulo = valor
        else:
            raise ValueError("El título debe ser un texto válido")
    
    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._autor = valor
        else:
            raise ValueError("El autor debe ser un texto válido")
    
    @property
    def isbn(self) -> str: # 9785.123.457-1
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._isbn = valor
        else:
            raise ValueError("El ISBN debe ser un texto válido")
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance(valor, float) and valor > 0:
            self._precio = valor
        else:
            raise ValueError("El Precio debe ser un número entero o c/decimales")
    
    def __repr__(self) -> str:
        return(
            f"Libro(titulo='{self._titulo}', autor='{self._autor}', "
            f"ISBN='{self._isbn}', precio='{self._precio}')"
        )
    
def main() -> None:
    libro = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "321-456-987-1", 100000.00)
    
    print("\n*** Información del Libro ***\n")
    
    print(libro)
    libro.precio = 185500.00
    libro.titulo = "100 años de soledad"
    
    print("\n*** Datos de Libro actualizados ***\n")
    print(libro)
    
    print("\n<< Programa finalizado >>>\n")
    
if __name__ == "__main__":
    main()
    