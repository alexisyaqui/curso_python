"""
ingrese 6 numeros en una lista y obtenga el numero mayor y menor ingresado

"""
# Ingresar Datos / Lista
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))
num4 = int(input('Número 4: '))
num5 = int(input('Número 5: '))
num6 = int(input('Número 6: '))

numeros = []
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)
numeros.append(num5)
numeros.append(num6)

mayor = menor = numeros[0]

for numeros in numeros:
    if numeros < menor:
        menor = numeros
    elif numeros > mayor:
        mayor = numeros

print('los numeros mayores son:', mayor)
print('los numeros menores son:', menor)
