print("adinvina el numero secreto")
numero_secreto = 7

while True:
    numero = int(input("ingrese un numero: "))
    if numero == numero_secreto:
        print("felicidades, adivinaste el numero secreto")
        break
    elif numero < numero_secreto:
        print("el numero es mayor, intentalo de nuevo")
    else:
        print("el numero es menor, intentalo de nuevo")