"""
Practica 03: Generador de contraseñas
Crear un sistema que genere una contraseña aleatoria

Para solucionar este problema se requiere listas, listas mayúsculas,
lista de minúsculas, lista de números y lista de símbolos y luego armar una
contraseña aleatoria sacando caracteres de estas listas.


"""
import random
def generador_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    signos = [',', '?', '=', '_', '/', '+', '*']

    caracteres = mayusculas + minusculas + numeros + signos
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def main():
    contrasena = generador_contrasena()
    print('tu contraseña es: ', contrasena)

if __name__ == '__main__':
    main()