suma = 0 
cantidad = 0 

nota = float(input("ingrese la nota (-1 para terminar): "))

while nota != -1:
    suma += nota
    cantidad += 1
    nota = float(input("ingrese la nota (-1 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print("el promedio es:", promedio)
else:
    print("no se ingresaron notas")