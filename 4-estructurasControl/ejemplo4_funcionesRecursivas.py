# factorial

def factorial(n):
    print("valor inicial => ", n)
    if n > 1:
        n = n * factorial(n - 1)
    print("valor final => ", n)
    return n


n = int(input("ingrese el numero: "))

f = factorial(3)
print(f'su factorial es {n} ', f)