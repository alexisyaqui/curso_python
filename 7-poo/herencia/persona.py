#1definimos la clase
class Persona:
    # 2 creamos nuestro constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def detallePersona(self):
        print(f'Nombre: {self.nombre}, \nEdad: {self.edad}')

    def __str__(self):
        return f'Nombre: {self.nombre}, \nEdad: {self.edad}'


# 3 creamos otra clase para hacer una herencia
class Cliente(Persona):
    pass

#clase empleado que hereda de persona
class Empleado(Persona):
    #creamos nuestro constructor
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    #creamos el detalle del empleado
    def detalleEmpleado(self):
        super().detallePersona()
        print('sueldo:', self.sueldo)

        #retorna el estado del objeto
    def __str__(self):
        return super().__str__() + f'\n Sueldo: {self.sueldo}'
        