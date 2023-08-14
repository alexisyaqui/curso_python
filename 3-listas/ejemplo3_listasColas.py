# También es posible utilizar una lista como una cola, donde el primer elemento agregado es el
# primer elemento recuperado ("primero en entrar, primero en salir");

#para implementar una cola hay que usar collections.deque
from collections import deque
cola = deque(["Erick", "Jhon", "Michael"])
cola.append("Terry")
cola.append(("Graham"))
cola.popleft()
print(cola)
print("\n")

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

print("\n")

squares = list(map(lambda x: x**2, range(10)))
print("\n")
squares = [x**2 for x in range(10)]
print(squares)
print("\n")

#comprensiones de listas anidadas

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
[[row[i] for row in matrix] for i in range(4)]
transportador = []
for i in range(4):
    transportador.append([row[i] for row in matrix])
    print(transportador)
print("\n")


#la declaracion
a = [-1, 1, 66.25, 333, 333, 1234,.5]
del a[0]
print(a)
del a[2:4]
print(a)

del a[:]
print(a)