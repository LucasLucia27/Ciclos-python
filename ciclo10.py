suma = 0

n = int(input("ingrese la cantidad de numeros a sumar: "))
for i in range(1,n+1):
    numero =int(input("ingrese un numero: "))
    suma += numero
print("la suma de los numeros ingresados es:", suma)
