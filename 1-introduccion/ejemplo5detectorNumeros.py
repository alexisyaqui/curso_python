# Crear un sistema que detecte si numero es par positivo o par negativo y tambien si es impar positivo o negativo y
#si el numero ingresado es 0 que detecte si es neutro.

#datos entrada
# numero par positivo y negativo
#numero impar positivo y negativo
# numero neutro

numero = int(input("ingrese el numero"))

if numero == 0:
    if numero > 0 and numero //2:
        print("el numero es mayor a 0 y es positivo ")
        if numero < 0 and numero // 2:
            print("el numero es negativo impar")
        else:
            print("el numero es ")