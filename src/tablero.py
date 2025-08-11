class PosOcupadaException(Exception):
    ...

class Tablero:
    def __init__(self):
        # matriz 3x3: "" para casilla vacía, "X" o "0" para ocupadas
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil: int, col: int, ficha: str):
        # indices válidos 0..2
        if not (0 <= fil <= 2 and 0 <= col <= 2):
            raise IndexError("Fila y columna deben estar entre 0 y 2.")
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posicion ocupada!")

    def esta_lleno(self) -> bool:
        for fila in self.contenedor:
            for c in fila:
                if c == "":
                    return False
        return True

    def reiniciar(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def __str__(self):
        # representa el tablero en formato legible
        filas = []
        for i, fila in enumerate(self.contenedor):
            fila_mostrable = " | ".join([c if c != "" else " " for c in fila])
            filas.append(f" {fila_mostrable} ")
            if i < 2:
                filas.append("---+---+---")
        return "\n".join(filas)
