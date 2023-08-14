"""
para declara una funcion se utiliza la palabra def
"""

def saludar():
    global nombre
    nombre = 'Juan Lopez'
    edad = 25
    return ('hola desde lan funcion saludar', nombre, edad)


valor = saludar()
saludo, nombre, edad = saludar()
print(valor)
print(saludo)
print(nombre, edad)