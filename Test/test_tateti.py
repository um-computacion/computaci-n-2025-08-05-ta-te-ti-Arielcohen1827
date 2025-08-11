import unittest
from src.tateti import Tateti
from src.jugador import Jugador

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.j1 = Jugador("Ana", "X")
        self.j2 = Jugador("Beto", "0")
        self.juego = Tateti(self.j1, self.j2)

    def test_ocupar_casilla_cambia_turno(self):
        turno_inicial = self.juego.turno
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertNotEqual(turno_inicial, self.juego.turno)

    def test_revisar_ganador(self):
        # Victoria en fila
        self.juego.tablero.contenedor = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
        self.assertEqual(self.juego.revisar_ganador(), "X")

    def test_asignar_victoria(self):
        self.juego.asignar_victoria("X")
        self.assertEqual(self.j1.victorias, 1)
        self.juego.asignar_victoria("0")
        self.assertEqual(self.j2.victorias, 1)

    def test_reiniciar_ronda(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.reiniciar_ronda()
        self.assertEqual(self.juego.turno, "X")
        self.assertEqual(self.juego.tablero.contenedor, [["", "", ""], ["", "", ""], ["", "", ""]])
