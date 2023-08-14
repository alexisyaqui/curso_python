
"""
parametros y argumentos en una funcion

"""

def suma(a, b):
    return a +b

def resta(a, b):
    if a == None or b == None:
        return a - b
    return

def multiplicar(a, b):
    return a * b

sumar = suma(23, 89)
print(f'la suma es', sumar)

restar = resta(34, 32)
print(f'la resta es: ', restar)

multiplo = multiplicar(23,2)
print(f'la multiplicacion es: {multiplo}')