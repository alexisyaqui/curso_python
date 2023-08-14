#Dado un rango de numeros enteros, obtener la cantidad de numeros enteros que contiene

ninicial = int(input("ingrese un numero: "))
nFinal = int(input("ingrese numero final numero: "))

i = 0
contador = 0
i = ninicial + 1
while  i < nFinal:
    contador += 1
    i += 1

print("Cantidad: ", contador)
