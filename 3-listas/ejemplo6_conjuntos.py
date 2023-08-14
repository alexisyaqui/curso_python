#conjunto no puede almacenar un valor que se repita
#un conjunto se define con set
a = set()
print(type(a))

b = set('adacababra')
c = set('alacazam')
print(b)
print(c)

print(a-b)
print(a|b)
print(a&b)
print(a^b)