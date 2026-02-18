from pathlib import Path
from typing import List

class FileManager:
    def __init__(self, file_path: str) -> None:
        self._path = Path(file_path)
        self._ensure_file()
        
    def _ensure_file(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.touch(exist_ok=True)
    
    def read_lines(self)-> List[str]:
        try:
            with self._path.open("r",encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except OSError as error:
            raise RuntimeError("Error leyendo el archivo")
    
    def append_line(self, text: str) -> None:
        if "\n" in text:
            raise ValueError("El texto, no debe contener saltos de linea")
        
        try:
            with self._path.open("a", encoding="utf-8") as file:
                file.write(text + "\n")
        except OSError as error:
            raise RuntimeError("Error escribiendo el archivo")
        