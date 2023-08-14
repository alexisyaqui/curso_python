class Persona():
    #artibuto privado se usa doble guion bajo __ejemplo
    __nombre = None
    __edad = None

    #ejemplo self.__ejemplo = ejemplo
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __metodoPrivado(self):
        print('Soy un metodo privado')

    #se crean objetos publicos con get y set
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

        #
    def __str__(self):
        return f'nombre: {self.__nombre} \n edad: {self.__edad}'