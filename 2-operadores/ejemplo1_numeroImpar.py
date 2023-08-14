# sentencia If
# Crear un sistema que detecte si numero es par positivo o par negativo y tambien si es impar positivo o negativo y
# si el numero ingresado es 0 que detecte si es neutro.

# datos entrada
# numero par positivo y negativo
# numero impar positivo y negativo
# numero neutro

numero = int(input("ingrese el numero: "))

if numero != 0:
    if numero > 0:
        if numero % 2 == 0:
            print(f'el numero {numero} es Par positivo')
        else:
            print(f'el numero {numero} es Impar positivo')
    else:
        if numero % 2 == 0:
            print(f'el numero es {numero} Impar positivo')
        else:
            print(f'el numero es {numero} Impar Negativo')
else:
    print(f'el numero es {numero} NEUTRO')
