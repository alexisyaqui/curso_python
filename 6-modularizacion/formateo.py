from sys import argv

if len(argv) == 4:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])

    # print(f'Nombre: {nombre} \n Edad: {edad} \n {altura}')
    # print('Nombre: {} \n Edad: {} \n Altura: {}'.format(nombre, edad, altura))
    # print(f'Nombre: {n} \n Edad: {e} \n Altura: {a}'.format(n=nombre, e=edad, a=altura))
    print('Nombre: %s \nEdad: %i \n%f'%(nombre, edad, altura))
else:
    print('ingrese los parametros correctamente')
    print(f'Ejemplo: formateo.py "Nombre", 25, 1.67')