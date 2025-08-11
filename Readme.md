# Proyecto Ta-Te-Ti en Python

**Alumno:** *Ariel Cohen*

## 📌 Descripción
Este proyecto es una implementación del clásico juego **Ta-Te-Ti** (Tic-Tac-Toe) en Python.  
Incluye:
- Interfaz de línea de comandos para jugar entre dos personas.
- Gestión de turnos y marcador.
- Validación de jugadas y detección de ganador o empate.
- Suite de tests unitarios para asegurar el correcto funcionamiento.

---

## ▶️ Cómo ejecutar el juego
python -m src.cli

## ▶️ Cómo ejecutar los test
python -m unittest discover -s test -p "test_*.py"

## ▶️ Cómo ejecutar los test individuales
python -m unittest test.test_jugador

python -m unittest test.test_tablero

python -m unittest test.test_tateti

python -m unittest test.test_cli


