from .tablero import Tablero

class Tateti:
    def __init__(self, jugador_x=None, jugador_0=None):
        # turno guarda 'X' o '0'
        self.turno = "X"
        self.tablero = Tablero()
        # jugadores opcionales (objetos Jugador), pueden asignarse externamente
        self.jugador_x = jugador_x
        self.jugador_0 = jugador_0

    def ocupar_una_de_las_casillas(self, fil: int, col: int):
        # intenta poner ficha en tablero (puede lanzar excepciones)
        self.tablero.poner_la_ficha(fil, col, self.turno)
        # después de colocar, chequeamos si hay ganador o empate en el llamador (CLI)
        # finalmente cambiamos turno
        self.turno = "0" if self.turno == "X" else "X"

    def revisar_ganador(self):
        t = self.tablero.contenedor
        lines = []

        # filas
        for r in range(3):
            lines.append([t[r][0], t[r][1], t[r][2]])
        # columnas
        for c in range(3):
            lines.append([t[0][c], t[1][c], t[2][c]])
        # diagonales
        lines.append([t[0][0], t[1][1], t[2][2]])
        lines.append([t[0][2], t[1][1], t[2][0]])

        for line in lines:
            if line[0] != "" and line[0] == line[1] == line[2]:
                return line[0]  # "X" o "0"

        return None

    def asignar_victoria(self, simbolo: str):
        if simbolo == "X" and self.jugador_x:
            self.jugador_x.sumar_victoria()
        elif simbolo == "0" and self.jugador_0:
            self.jugador_0.sumar_victoria()

    def reiniciar_ronda(self):
        self.tablero.reiniciar()
        self.turno = "X"
