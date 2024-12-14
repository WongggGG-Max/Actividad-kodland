import random

Tamano = int(input('crea una contraseña, de 10 letras o numeros'))
caracteres =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

x = ""
for i in range(Tamano):
    y = random.choice(caracteres)
    x += y
print(x)
