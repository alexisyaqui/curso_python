"""
Enunciado: debido a los excelentes resultados, el restaurante decide ampliar
sus ofertas de acuerdo a la siguiente escala de consumo, ver la tabla. Determinar el
monto del descuento, el importe del impuesto y el importe a pagar.

Consumo (S/.)       Descuento (%)
Hasta 100                 10
Mayor a 100             20
Mayor a 200             30

datos de entrada
descuento menor de 100.00 es el 10%
descuento mayor a 100.00 es el 20%
impuesto para ambos es el 19%
"""

print("**" * 20)
print("\t CONSUMO DE RESTAURANTE")
print("**" * 20)
consumo = float(input("ingrese el consumo de la persona: "))

montoDescuento = 0
impuesto = 0
importePagar = 0

if consumo >= 0:
    if consumo <= 100:
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200:
        dato_descuento = '30%'
        descuento = consumo * 0.30

    montoDescuento = consumo - descuento
    impuesto = montoDescuento * 0.19
    importePagar = montoDescuento + impuesto

    print("==" * 10)
    print("FACTURA")
    print("==" * 10)
    print("Decuento por la cantidad $", dato_descuento)
    print('el monto del Descuento es $', montoDescuento)
    print('el impuesto es $', impuesto)
    print('el importe a pagar  es $', importePagar)

else:
    print("el Consumo tiene que ser mayor a $. 0.00")
