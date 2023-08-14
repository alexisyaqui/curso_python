#un restaurante ofrece un descuento del 10% para el consumo
#de hasta s/ 100.00 y un descuento del 20% para consumos mayores, para
#para ambos casos se aplica un descuento del 19%.
#determinar el monto del descuento, el impuesto y el importe a pagar.

"""
datos de entrada
descuento menor de 100.00 es el 10%
descuento mayor a 100.00 es el 20%
impuesto para ambos es el 19%
"""
print("**"*20)
print("\t CONSUMO DE RESTAURANTE")
print("**"*20)
consumo = float(input("ingrese el consumo de la persona: "))

montoDescuento = 0
impuesto = 0
importePagar = 0

if consumo <= 100:
    dato_descuento = '10%'
    descuento = consumo * 0.10
elif consumo > 100:
    dato_descuento = '20%'
    descuento = consumo * 0.20

montoDescuento = consumo - descuento
impuesto = montoDescuento * 0.19
importePagar = montoDescuento + impuesto


print("=="*10)
print("FACTURA")
print("=="*10)
print('el monto del Descuento es;', montoDescuento)
print('el impuesto es;', impuesto)
print('el importe a pagar  es;', importePagar)



