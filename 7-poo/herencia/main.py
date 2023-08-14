#creamos nuestros

from persona import Cliente, Empleado

# cliente1 = Cliente('Juan', 23)
# cliente2 = Cliente('Luis', 54)
#
# cliente1.detallePersona()
# print(cliente2)

empleado1 = Empleado('Juan', 34, 15.00)
empleado2 = Empleado('Luis', 24, 1500)

empleado1.detallePersona()
empleado1.detalleEmpleado()
print(empleado1)