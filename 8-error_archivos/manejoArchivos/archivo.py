from io import open
from os import path

def escribirArchivo():
    # w para escribir
    archivo = open('texto.txt', 'w')
    archivo.write('Hola mundo de python')
    archivo.close()


def leerArchivo():
    if path.isfile('texto.txt'): #path.isfile es poara comprobar si existe el archivo
        archivo = open('texto.txt', 'r') #se abre el archivo con 'r' de read
        #textos = archivo.read() para leer todo el contenido del archivo
        textos = archivo.readline() #para leer una sola linea
        archivo.close() #siempre tenemos que cerrar el archivo

        print(textos) #imprime la lectura del archivo por medio de una variable
    else:
        print('no existe el archivo')

def agregarDatos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a')
        archivo.write('\n bienvenido al curso de python, archivos')
        archivo.close()

        print('dato agregado')

    else:
        print('el archivo no existe')


def modificarDatos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+')
        texto = archivo.readlines() #leemos todas las lineas del archivo
        print(texto)

        texto[1] = 'Hola Alexis Yaqui'
        print(texto)
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
        print(texto)
    else:
        print('el archivo no existe')


def eliminarDatos():
    archivo = open('texto.txt', 'w')
    archivo.close()



# escribirArchivo()
# leerArchivo()
# agregarDatos()
# modificarDatos()
eliminarDatos()