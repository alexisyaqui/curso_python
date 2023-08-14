"""
Crear un sistema que detecte si un numero es primo o no Para solucionar este problema se
requiere que el usuario ingres un numero por teclado y el sistema detecte si es primo o no.
Un numero primo es aquel que se puede dividir solo dos veces por 1 y por sí misma.


"""


def primalidad(numero):
    #creamos un contador
    contador = 0

    #usamos el for para recorrer el rango en que va ser divisible
    for i in range(1, numero + 1):
        #validamos si el rango es divisible dentro de uno o es divisible entre el mismo numero
        if i == 1 or i == numero:
            #si es divisible dentro de uno y el mismo numero pasa a la siguiente operacion
            continue

            #veririfica si el numnero sigue siendo a 0 entonces escoge a otro numero para la operacion
        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False


def main():
    numero = int(input("ingrese el numero: "))

    primo = primalidad(numero)
    if primo:
        print('es primo ')
    else:
        print('no es primo: ')


if __name__ == '__main__':
    main()
