from figuras import Rectangulo, Circulo, probarFigura


def main():
    while True:
        menu = """
        FIGURAS
        1. Rectangulo
        2. Circulo
        3. Salir
        Ingrese una Opcion
        """
        opcion = input(menu)

        if opcion == '1':
            print("*" * 10)
            print("CALCULAR EL RECTANGULO")
            print("*" * 10)

            base = float(input("ingrese la Base: "))
            altura = float(input("ingrese la Altura: "))
            r = Rectangulo(base, altura)
            probarFigura(r)

        elif opcion == '2':
            radio = float(input("ingrese Radio: "))
            c = Circulo(radio)
            probarFigura(c)

        elif opcion == '3':
            print("Saliendo del sistema")
            break
        else:
            print("menu incorrecto")


if __name__ == '__main__':
    main()
