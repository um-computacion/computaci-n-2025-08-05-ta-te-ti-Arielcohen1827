import unittest
from src.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_poner_ficha_valida(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_posicion_ocupada(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, "0")

    def test_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.tablero.poner_la_ficha(3, 0, "X")
        with self.assertRaises(IndexError):
            self.tablero.poner_la_ficha(0, 5, "X")

    def test_esta_lleno(self):
        for i in range(3):
            for j in range(3):
                self.tablero.poner_la_ficha(i, j, "X")
        self.assertTrue(self.tablero.esta_lleno())

    def test_reiniciar(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.reiniciar()
        self.assertEqual(self.tablero.contenedor, [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_str(self):
        self.assertIsInstance(str(self.tablero), str)
