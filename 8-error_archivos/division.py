divi = 0

try:
    a = int(input("ingrese el dividendo: "))
    b = int(input("ingrese el divisor: "))

    divi = a / b

    #el valuelError no acepta caracteres solo numeros
except ValueError:
    print('Error!, ingrese solo numeros enteros, no se aceptan letras')
    #no acepta que ele divisor sea divido entre 0
except ZeroDivisionError:
    print('Error!, el divisor no puede ser divido entre 0')
    #el Exception as error junto con el type(error).__name__ devuelve la clase de error
except Exception as error:
    print('ha ocurrido un error no previsto: ', type(error).__name__)

print("la division es: ", divi)