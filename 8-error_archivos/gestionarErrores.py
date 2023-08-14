c = 0
suma = 0
while c < 3:
    try:
        n = int(input(f'ingrese un numero {c+1}: '))
        suma += n
        c += 1
    except:
        print("ingrese solo numeros enteros")
    else:
        print("funcionando correctamente")
    finally:
        print("fin de la ejecucion")

print("el resultado de la suma: ", suma)
