# Diccionarios van entre corchetes

numeros = {}
print(numeros)
numeros = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
print(numeros)
# para eliminar un valor en el diccionario se usa del
print("eliminar un elemento con del, (cuatro)")
del numeros['cuatro']
print(numeros)

# para actualizar el diccionario se utiliza list
print("para acutualizar el diccionario se usa list")
list(numeros)
print(numeros)

# para ordenar se utiliza sorted(d)
print("para ordenar el diccionario se utiliza sorted")
sorted(numeros)
print(numeros)

print("para verificar si existe el elemnto en el didccionario se usa in")
'uno' in numeros
print(numeros)
print("\n")

# para agregar otro dato en el diccionario
numeros['cinco'] = 5

print(numeros)

busqueda = numeros.get('seis', "no se encontro")
print(busqueda)

print("para crear diccionarios directamente se usa dict")
nuevoDiccionario = dict([('sape', 234), ('guido', 42432), ('jack', 432423)])
print(nuevoDiccionario)

# Tecnicas de bucle
print("TECNICAS DE BUCLE CON ITEMS")
pelea = {'Muatai': 'india', 'artex mixtas': 'usa', 'boxeo': 'americano'}
for k, l in pelea.items():
    print(k, l)
# Muatai india
# artex mixtas usa
# boxeo americano# Tecnicas de bucle
print("recorrer una secuencia, el indice de poscion, con enumerate")
for i, v in enumerate(['tic', 'tac', 'toc', 'tuc']):
    print(i, v)
    # 0 tic
    # 1 tac
    # 2 toc


print("recorrer dos o mas secuencias al mismo tiempo y emparejar con ZIP()")
preguntas = ['nombre', 'apellido', 'direccion', 'telefono', 'genero']
respuestas = ['Juan', 'Lopez', 'easdfas', '342334223', 'hombre']
for m, n in zip(preguntas, respuestas):
    print('La pregunta es: {0}? la respuesta es: {1}.'.format(m,n))
    print("\n")


#FUNCION REVERSED
print("recorrer de forma inversa, primero recorra hacia adelante despues use la funcion de reverse")
nuevoDiccionario = dict([('sape', 234), ('guido', 42432), ('jack', 432423)])

for i in reversed(nuevoDiccionario):
    print(i)