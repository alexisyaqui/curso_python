objetos de lista en python
list.add() = agrega un elemento al final de la lista a .[len(a)] = [x]
list.extend() = amplia la lista agregando todos los elementos a.[len(a)]
list.insert() = inserta un elemento en una posicion determinada, el primero es el indice, inserta al principio
list.remove() = elimina el primer elemento de la lista cuyo valor es igual a x, cuando no existe evalua valueError
list.pop([i]) = retira el articulo en la poscion dada en la lista y devuelve, si no se especifica en con pop, se elimina
y devuelve el ultimo
list.clear() = elimina todos los elementos de la lista. equivalente .del a[:]
list.index(x[, start [, end]]) = devuelve el indice basado en cero en la lista del primer elemento cuyo valor es igual a
x
list.count(x) = devuelve el numero de veces que x aparece en la lista
list.sort(* , vlace = ninguno, inverso = falso) = ordena los elementos de la lista en su lugar, los argumentos se pueden
personalizar la ordenacion.
list.reverse() = invierte los elementos de la lista en su lugar
list.copy() = devuelve una copia superficial de la lista equivalente a [:]