class Jugador:
    def __init__(self, nombre: str, simbolo: str):
        """
        nombre: nombre del jugador (str) - NO puede estar vacío
        simbolo: 'X' o '0' (string)
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del jugador no puede estar vacío.")
        self.nombre = nombre.strip()
        self.simbolo = simbolo
        self.victorias = 0

    def sumar_victoria(self):
        self.victorias += 1

    def __repr__(self):
        return f"{self.nombre} ({self.simbolo}) - Victorias: {self.victorias}"
