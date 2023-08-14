
#creamos nuestra clase
class Persona:
    #creamos nuestro constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def detallePersona(self):
        print(f'Nombre:  {self.nombre} \nEdad: {self.edad}')

    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'

class Cliente(Persona):
    pass

class Empleado(Persona):
    #creamos el constructor
    def __init__(self, nombre, edad, sueldo):
        ###OJO OJO OJO#####

        # super().__init__(nombre, edad)
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

    def detalleEmpleado(self):
        ###OJO OJO OJO#####
        # super().detallePersona()
        Persona.detallePersona(self)
        print(f'Sueldo: {self.sueldo}')

    def __str__(self):
        ###OJO OJO OJO#####
        # return super().__str__() + f'\n sueldo: {self.sueldo}'
        return Persona.__str__(self) + f'\n sueldo: {self.sueldo}'