import math

class Figura():
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * self.base + 2 * self.altura * 2

    def __str__(self):
        return f'Nombre: {self.nombre}, \t Base: {self.base} \t Altura: {self.altura}'


class Circulo():
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f'Nombre: {self.nombre}, \t Radio: {self.radio}'


def probarFigura(figura):
    print(figura)
    print('Area: ', figura.area())
    print('Perimetro: ', figura.perimetro())
