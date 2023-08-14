# argumentos indeterminados
# args argumentos por poscicio
# **kwargs, argmumentos indeterminados por posicion
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs


sum_total, datos = sumar(1, 12, 13, 45, 45, 6, 74, nombre='alex', edad=20)
print('la suma tottal es:', sum_total)
print('datos es:', datos)

