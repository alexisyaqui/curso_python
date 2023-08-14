
class OperadorExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def dividir(a, b):
    if b == 0:
        raise OperadorExcepcion('Error, no se puede dividir por cero')
    else:
        return a /b

dividir(5,0)
