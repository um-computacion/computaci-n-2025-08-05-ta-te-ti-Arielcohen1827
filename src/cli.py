import random
from .tateti import Tateti
from .jugador import Jugador
from .tablero import PosOcupadaException


def pedir_entero_con_prompt(prompt):
    while True:
        try:
            v = int(input(prompt))
            return v
        except ValueError:
            print("Ingrese un número entero válido (0, 1 o 2).")

def asignar_simbolos_aleatorios(j1, j2):
    if random.choice([True, False]):
        j1.simbolo = "X"
        j2.simbolo = "0"
    else:
        j1.simbolo = "0"
        j2.simbolo = "X"

def alternar_simbolos(j1, j2):
    j1.simbolo, j2.simbolo = j2.simbolo, j1.simbolo

def mostrar_marcador(j1, j2):
    print("\nMarcador:")
    print(f"{j1.nombre}: {j1.victorias}")
    print(f"{j2.nombre}: {j2.victorias}")

def main():
    print("Bienvenidos al Tateti \n")

    while True:
        try:
            nombre1 = input("Nombre Jugador 1: ")
            j1 = Jugador(nombre1, "")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            nombre2 = input("Nombre Jugador 2: ")
            j2 = Jugador(nombre2, "")
            break
        except ValueError as e:
            print(e)


    # Primera ronda → símbolos aleatorios
    asignar_simbolos_aleatorios(j1, j2)

    # Crea el juego con turno inicial siempre "X"
    juego = Tateti()
    juego.jugador_x = j1 if j1.simbolo == "X" else j2
    juego.jugador_0 = j2 if j1.simbolo == "X" else j1
    juego.turno = "X"

    ronda = 1

    while True:
        print(f"\n--- Ronda {ronda} ---")
        print(f"{j1.nombre} ({j1.simbolo}) vs {j2.nombre} ({j2.simbolo})\n")
        print(juego.tablero)
        print(f"\nTurno de: {juego.turno} "
              f"({juego.jugador_x.nombre if juego.turno == 'X' else juego.jugador_0.nombre})")

        try:
            fil = pedir_entero_con_prompt("Ingrese fila (0-2): ")
            col = pedir_entero_con_prompt("Ingrese col (0-2): ")
            if not (0 <= fil <= 2 and 0 <= col <= 2):
                print("Fila y columna deben estar entre 0 y 2.")
                continue

            juego.ocupar_una_de_las_casillas(fil, col)

            ganador = juego.revisar_ganador()
            if ganador:
                juego.asignar_victoria(ganador)
                print("\n¡Hay ganador!")
                print(f"Ganó {juego.jugador_x.nombre if ganador == 'X' else juego.jugador_0.nombre} ({ganador})")
                print("\nTablero final:")
                print(juego.tablero)
                mostrar_marcador(j1, j2)

                resp = input("\n¿Jugar otra ronda? (s/n): ").strip().lower()
                if resp.startswith("s"):
                    ronda += 1
                    alternar_simbolos(j1, j2)
                    juego.reiniciar_ronda()
                    juego.jugador_x = j1 if j1.simbolo == "X" else j2
                    juego.jugador_0 = j2 if j1.simbolo == "X" else j1
                    continue
                else:
                    print("\nGracias por jugar.")
                    break

            if juego.tablero.esta_lleno():
                print("\nEmpate (tablero lleno).")
                print("\nTablero final:")
                print(juego.tablero)
                mostrar_marcador(j1, j2)

                resp = input("\n¿Jugar otra ronda? (s/n): ").strip().lower()
                if resp.startswith("s"):
                    ronda += 1
                    alternar_simbolos(j1, j2)
                    juego.reiniciar_ronda()
                    juego.jugador_x = j1 if j1.simbolo == "X" else j2
                    juego.jugador_0 = j2 if j1.simbolo == "X" else j1
                    continue
                else:
                    print("\nGracias por jugar.")
                    break

        except PosOcupadaException:
            print("La posición ya está ocupada, intentá otra.")
        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    main()
