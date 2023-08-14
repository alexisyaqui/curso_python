"""
ractica 04: Conversor de Monedad
Crear un sistema que convierta de moneda nacional a dólares por
ejemplo de soles peruanos a dólares, pesos mexicanos a dólares, pesos colombianos a dólares.

Para solucionar este problema se requiere que el usuario ingrese la cantidad de
monedas nacionales y luego realizar la conversión.
Para este sistema debe hacer un menú de navegación para seleccionar a que tipo de moneda se para
 la conversión y también para cerrar el programa, el sistema no se debe cerrarse si no lo deseas.

datos entrada
moneda nacional a dolar
pesos mexicanos a dolar
pesos colombianos a dolares
"""


def conversion(valorMoneda, pais):
    cantidadMoneda = float(input(f'ingrese la cantidad de dinero del {pais}: '))

    dolares = cantidadMoneda / valorMoneda
    dolares = round(dolares, 2)
    print(f'la cantidad de dinero es $. {dolares}')


def main():
    while True:
        menu = """
        1. Soles Peruanos a Dolares
        2. Pesos Mexicanos a Dolares
        3. Pesos Colombianos a Dolares
        4. Salir
        Ingrese una opcion"""
        opcion = input(menu + ' ')

        if opcion == '1':
            convertir = conversion(0.27236027, 'soles peruanos')
        elif opcion == '2':
            convertir = conversion(0.058571494, 'Pesos Mexicanos')
        elif opcion == '3':
            convertir = conversion(0.00024, 'Pesos Colombianos')
        elif opcion == '4':
            print("Saliendo.. Vuelva Pronto!!!")
            break
        else:
            print("opcion incorrecta, vuela a seleccionar el menu, permitido de 1 al 4")


if __name__ == '__main__':
    main()
