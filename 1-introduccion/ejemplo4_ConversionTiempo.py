#Crear un programa que permita convertir una cantidad de segundos en horas, minutos, y segundos.

cantidad = int(input("ingrese la cantidad de tiempo: "))

horas = cantidad // 3600
horasSobrante = cantidad % 3600

minutos = horasSobrante // 3600
minutosSobrante = horasSobrante % 60

print(f'la cantidad de horas, minutos, segundos son: \n Hora: {horas},\n minuto: {minutos}, \n segundos: {minutosSobrante}')

