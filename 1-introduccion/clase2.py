# ESTRUCTURA DE DATOS

# python cuenta con numeros reales, complejos, ademas pueden ser representados en decinaml, binario, octal y hexadecimal.

numero_entero = 8

# tambien puede ser representado como numero negativo
numero_negativo = -78

# por otro lado puede ser un numero real.
numero_real = 3.4

# numero complejo, son aquellos formados por una parte real y otra imaginaria
numero_complejo = 3.2 + 7j

# siendo una valida expresion
numero_complex = 5J + 3

################################################
# EXPRESION CON OPERADOR
################################################
###
# a + b = suma
# a - b = resta
# a * b = multiplicacion
# a % b = resto de una division o mas conocido como modulo
# a / b = division real
# a // b = division entera
# a ** b = potencia
# a | b = OR (bit)
# a ^ b = XOR (bit)
# a & b = AND (bit)
# a == b = igualdad
# a != b = desigualdad
# a or b = OR (logica)
# a andb b = AND (logica)
# not a = negacion (logica)
##

################################################
# FUNCIONES MATEMATICAS
# raiz cuadrada, calculo del valor maximo y minimo de una lista o el redondo de para numeros reales
# operaciones trigonometricas, seno, coseno y tangente.
#
# Lo cual para poder utilizar esas funciones es necesario importar la funcion math.

# import math
# abs(47-54)
################################################
import math

# para la raiz cuadrada de 169 es
print("la raiz cuadrada de 169 es: ", math.sqrt(169))

# para pasar de decimal a binario o de octal a hexadecimal, python tiene las funciones int(), oct(), bin()

print("el exadecimal de 16 es: ", hex(16))

print("el octal de 8 es: ", hex(8))
print("el binario de 0xfe es: ", bin(0xfe))

################################################
# CONJUNTOS
################################################
# LA FUNCION CONJUNTOS SE UTILIZA CON SET

conjunto = set('845')
print("el conjunto es: ", conjunto)

# un conjunto tambien puede ser definido por llaves
conjunto = {8, 4, 5}
print("el conjunto definido por llaves: ", conjunto)

# operaciones como union, interseccion, creacion de subconjuntos y diferencia
conjunto_2 = set('785')
interseccion = conjunto & conjunto_2
resultado = conjunto.intersection(conjunto_2)
print("\n")

duplicados = {2, 3, 4, 5, 6, 7, 8, 2, 4, }
print(duplicados)

################################################
# CADENAS DE TEXTOS
################################################
cadena = "esto es una cadena de texto"
cadena_multiple = """esta cadena de texto
tiene mad de una linea· en concreto cuenta con
tres lienas diferentes"""

################################################
# FUNCIONES Y METODOS DE CADENA DE TEXTO
################################################
#FUNCION LEN
print("funcion len")
cad = "Cadena de texto de ejemplo"
print("Cadena de texto de ejemplo: tiene: ", len(cad), "letras")
print("\n")

#FUNCION FIND
print("funcion find")
cad = "xyza"
print("de xyza: la z esta en la poscion:  ", cad.find("z"))
print("\n")

#FUNCION REPLACE
print("funcion replace")
cad = "hola mundo"
print("hola mundo: cambiar hola por adios:  ", cad.replace("hola", "adios"))
print("\n")

#LA FUNCION DE STRIP(), LSTRIP(), y RSTRIP()
#ayudaran a eliminar los espacios en blanco de izquierda a los que aparecen en la derecha
print("FUNCION DE STRIP(), LSTRIP(), y RSTRIP()")
cad = " cadena con espacio en blanco "
print("eliminando espacios lado: >>", cad.strip())
print("eliminando espacios lado: >>", cad.lstrip())
print("eliminando espacios lado: >>", cad.rstrip())
print("\n")

#LA FUNCION DE UPPER
#convierte todos los caracteres de una cadena de texto a mayusculas
print("FUNCION UPPER")
cad = " cadena con espacio en blanco "
cad3 = " CADENA EN MINISCULA "
print("upper convierte a todo en mayuscula", cad.upper())
print("lower convierte a todo en miniscula", cad3.lower())

print("\n")

#LA FUNCION DE CAPITALIZE()
#convierte el primer caracter de un string a Mayuscula
print("funcion capitalize")
cad = "un ejemplo"
print("primera letra en mayuscula: (un ejemplo) a >>", cad.capitalize())
print("\n")

#LA FUNCION SPLIT()
#elimina todas los ;
print("FUNCION SPLIT")
cad = "primer valor; segundo valor; tercer valor; cuarto valor"
print("eliminando los ; con split: >>", cad.split(";"))
print("\n")

#LA FUNCION JOIN()
#metodo que devuelve una cadena de texto, aparecen por serparados de una coma (,)
print("FUNCION JOIN")
cad = "abcdefegas".join(',')
print("separando con , la cadena con join. >>" + "abcdefegas".join(','))
print("\n")


################################################
# OPERACIONES
################################################
print("OPERACIONES")
cad_contact = "hola" + "mundo"
print((cad_contact))

cad = "Nueva cadena de texto"
"x " in cad
print(cad[3])
print(cad[:3])
print(cad[-3])
print(cad[3:])

################################################
# TUPLAS
################################################
print("TUPLAS")
t = (1,2,3,4)
print(t[1])
t = (1, ('a', 3), 5.6)
for elemento in t:
    print("recorriendo tupla", elemento)
    print("recorriendo tupla", )