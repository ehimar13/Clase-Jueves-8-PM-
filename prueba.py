import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("ingresa la longitud: "))

clave = ""

for i in range(longitud):
    caracter = random.choice(caracteres)
    clave += caracter

print("Contraseña generada:", clave)

