print("escribe cualquier palabra")
palabra = input("ingresa la palabra: ")
vocales = 0

for letra in palabra.lower():
    if letra in "aeiou":
        vocales += 1

print("la cantidad de vocales es:", vocales)