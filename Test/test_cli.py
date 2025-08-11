import unittest
from src.cli import asignar_simbolos_aleatorios, alternar_simbolos

class testjugador:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo
        self.victorias = 0

class TestCLI(unittest.TestCase):
    def test_asignar_simbolos_aleatorios(self):
        j1 = testjugador("A", "")
        j2 = testjugador("B", "")
        asignar_simbolos_aleatorios(j1, j2)
        self.assertIn(j1.simbolo, ["X", "0"])
        self.assertIn(j2.simbolo, ["X", "0"])
        self.assertNotEqual(j1.simbolo, j2.simbolo)

    def test_alternar_simbolos(self):
        j1 = testjugador("A", "X")
        j2 = testjugador("B", "0")
        alternar_simbolos(j1, j2)
        self.assertEqual(j1.simbolo, "0")
        self.assertEqual(j2.simbolo, "X")
