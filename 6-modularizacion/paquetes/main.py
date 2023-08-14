import my_paquete.aritmetica as a


def main():
    sumar = a.sumar(4,56,4,56,4,5,46)
    resta = a.restar(10,5)
    potencia = a.potencia(3,3)

    print(f'la suma es: {sumar}')
    print(f'la resta es: {resta}')
    print(f'la potencia es: {potencia}')

if __name__ == '__main__':
    main()