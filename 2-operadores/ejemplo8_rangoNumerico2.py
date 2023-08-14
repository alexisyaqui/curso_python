#Dado un rango de numérico entero num. inicial y num. fina,
# obtener la cantidad de números positivos y negativos que existen en el rango
#
valor1 = int(input("Numero Inicial: "))
valor2 = int(input("Numero final: "))

valor2 += 1
cantidadPositivos = 0
cantidadNegativos = 0

for numero in range (valor1, valor2):
    if numero % 2 == 0:
        cantidadPositivos += 1
    else:
        cantidadNegativos += 1

print("cantidad Positivos", cantidadPositivos)
print("cantidad Negativos", cantidadNegativos)
