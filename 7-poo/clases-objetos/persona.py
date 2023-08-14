
class Persona():

    #creamos un constructor y dentro del constructor van los atributos incluyendo self
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #metodos son comportamientos o acciones del objeto
    def mostrarDatos(self):
        print("*"*10)
        print("MOSTRAR DATOS")
        print('Nombre. ', self.nombre)
        print('Edad. ', self.edad)

    def __str__(self):
        return f'Nombre: {self.nombre} \n Edad: {self.edad}'