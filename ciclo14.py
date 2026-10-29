print("escribe hola o salir")
usuario = input("ingresa la palabra: ")
while usuario != "salir":
    if usuario == "hola":
        print("hola, como estas?")
    else:
        print("no entiendo lo que escribiste")
    usuario = input("ingresa la palabra: ")