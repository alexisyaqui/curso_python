#Dado 3 numeros, devolver los numeros en orden ascendente


a = int(input("ingrese el primer numero:  "))
b = int(input("ingrese el segundo numero:  "))
c = int(input("ingrese el tercer numero:  "))

cadena = [a, b, c]

cadena.sort()
for n in cadena:
    print(n)