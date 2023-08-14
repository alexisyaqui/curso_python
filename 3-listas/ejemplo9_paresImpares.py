"""
crear 2 listas y una tupla que tendra numeros de 1 a 9. la primera lista se llamara pares y el segundo impar
ambos numeros estaran vacias. despues multiplica cada uno de los numeros de la tupla por un numero aleatorio
entre 1 y 100, si el resultado es par guarda ese numero en la lista de pares y si es impar en la lista de impares.
muestra por consola: -la multiplicacion que se produce junto con su resultado con el formato 2x3=6 y la lista de
pares e impares.

DATOS DE ENTRADA
dos lista de numeros de 1 al 9
una tupla 1 al 9
numeros pares
numeros impares
multiplicacion
numero aleatorio  1 y 100

"""
import random

pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in numeros:
    numeros_random = random.randint(1, 100)
    resultado = i * numeros_random

    if resultado % 2 == 0:
        print(f'{i} x {numeros_random} = {resultado}')
        pares.append(resultado)
    else:
        print(f' {i} x {numeros_random} = {resultado}')
        impares.append(resultado)

print('los numeros pares son: ', pares)
print('los numeros impares son: ', impares)
