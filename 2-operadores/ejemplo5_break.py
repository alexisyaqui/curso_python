c = 0
while c < 10:
    c += 1
    print(c)

    if c == 5:
        # print("termina el bucle")
        print("salta a siguiente iteracion")
        # break
        continue
    print("despues del continue")
else:
    print("Fin del While")

print("\n")
print("**" * 20)
print("BREAK")
print("**" * 20)

cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("se encontro la letra h")
        break
        print("fin del ciclo", letra)

print("\n")
print("**" * 20)
print("CONTINUE")
print("**" * 20)

cadena2 = 'Python'

for letra2 in cadena2:
    if letra2 == 'P':
        print("se encontro la letra P")
        continue
    print(letra2)

print("\n")
print("**" * 20)
print("EJEMPLO")
print("**" * 20)

x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)


