import unittest
from src.jugador import Jugador
class TestJugador(unittest.TestCase):
    def test_nombre_valido(self):
        j = Jugador("Juan", "X")
        self.assertEqual(j.nombre, "Juan")
        self.assertEqual(j.simbolo, "X")
        self.assertEqual(j.victorias, 0)

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Jugador("", "X")
        with self.assertRaises(ValueError):
            Jugador("   ", "0")

    def test_sumar_victoria(self):
        j = Jugador("Maria", "0")
        j.sumar_victoria()
        self.assertEqual(j.victorias, 1)

    def test_repr(self):
        j = Jugador("Luis", "X")
        self.assertIn("Luis", repr(j))
        self.assertIn("X", repr(j))
