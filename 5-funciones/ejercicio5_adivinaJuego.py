"""
Practica 05: Juego – Adivina el numero
Crear un juego donde el sistema genere un numero aleatorio y el jugador intente adivinar el numero aleatorio.

Para crear este juego ten encueta los siguientes datos

          Difícil 5 intentos o vidas

          Intermedio 7 intentos o vidas

          Fácil 10 intentos o vidas

De acuerdo como va intentado el juego le debe dar una pista si el número es más grande o más pequeño.

También tiene que indicarle las vidas que le quedan.

random
contador
nivel 1
nivel 2
nivel 3



"""
import random


def jugar(vidas):
    numeroRandom = random.randint(1, 100)
    numeroElegido = None

    while numeroRandom != numeroElegido:
        numeroElegido = int(input('ingrese un numero entre 1 y 100: =>> '))

        if numeroRandom < numeroElegido:
            print('Elige un numero mas pequeño')
            vidas -= 1
        elif numeroRandom > numeroElegido:
            print('ingrese un numero mas grande')
            vidas -= 1
        if vidas == 0:
            print('!! GAME OVER !!')
            break

        print(f'Te quedan: {vidas}, vidas')

    if numeroElegido == numeroRandom:
        print("FELICIDADES!! ACERTASTE AL NUMERO")


def main():
    while True:
        menu = """
        ***********************
        ADIVINA EL JUEGO
        ***********************
        1. Nivel Uno (Facil).
        2. Nivel Dos (Intermdio).
        3. Nivel Tres (Avanzado-Dificil).
        4. Salir.
        Ingrese una Opcion
        """

        opcion = input(menu)
        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(3)
        elif opcion == '4':
            print("Saliendo del Juego!!!.")
            break
        else:
            print("SELECCIONE EL MENU CORRECTO DEL 1 AL 4")
            opcion = input(menu)

if __name__ == '__main__':
    main()
