#calcular el previo de venta.
# dado el valor de venta de productos, hallar el IGV(18%) y el precio de venta.


print("calcular el precio de venta.")
precioUnitario = float(input("ingrese el precio del producto: "))

igv = precioUnitario * 0.18
precioVenta = igv + precioUnitario

print(("="*25))
print('----- factura de venta-----')
print("="*25)
print('El valor de venta: ', precioUnitario)
print('El IGV: ', igv)
print('El precio de venta es: ', precioVenta)
print("="*25)