"""
crear un sistema que detecte si una palabra es palindroma o no

SOLUCION:
para solucionar este problema el usuario tiene que ingresar por pantalla
una palabra y el sistema verifique si es palindromo o no

una palabra palindroma se lee de igual forma como de la derecha e izquierda

DATOS DE ENTRADA
palabra
lista

"""

def palindromo(palabra):
    #eliminamos los espacios de la palabra u oracion
    palabra = palabra.replace(' ', '')
    #despues convertimos a miniscula o mayuscula la palabra u oracion
    palabra =  palabra.lower()
    palabra = palabra.upper()
    #ahora invertimos la palabra
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    #ingresamos la palabra por medio de teclado
    palabra = input("ingrese la palabra palindromo: ")

    #creamos el objeto
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('la palabra es palindroma')
    else:
        print('la palabra no es palindroma')

    return

if __name__ == '__main__':
    main()