#listas en python

print("****"*10)
print("\tLISTAS ESTRUCTURADAS EN PYTHON")
print("****"*10)

#lista normal
print("\tLISTAS NORMAL")
frutas = ['orange', 'manzana', 'pera', 'banano', 'kiwi', 'manzana', 'banano']
print("\n")

#lista contar
print("\tLISTAS COUNT")
print(frutas.count('manzana'))
print("\n")

#lista indice
print("\tLISTAS INDEX")
print(frutas.index('manzana'))
print(frutas.index('manzana', 4))
print("\n")

#lista inversa con reverse
print("\tLISTAS REVERSE")
frutas.reverse()
frutas
print(frutas)
print("\n")

#lista agregar
print("\tLISTAS APPEND")
frutas.append('durazno')
frutas
print(frutas)
print("\n")

#lista ordenar con sort
print("\tLISTAS SORT")
frutas.sort()
frutas
print(frutas)
print("\n")

#lista pop
print("\tLISTAS POP")
frutas.pop()
print(frutas)
print("\n")