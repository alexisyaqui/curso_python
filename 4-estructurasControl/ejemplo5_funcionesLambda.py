#funciones lambda son anonimas

sumar = lambda a, b:a + b
doblar = lambda n: n* 2
par = lambda n: n % 2 == 0
impar = lambda  n: n /2 !=0
revertir = lambda cadena: cadena[::-1]


print(sumar(34,34))
print(doblar(34))
print(par(4))
print(impar(7))
print(revertir('hola'))