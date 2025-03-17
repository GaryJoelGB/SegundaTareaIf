#Escribe un programa que pida al usuario que ingrese un número entero positivo. 
#El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.

numero = int(input("Ingrese un número positivo: "))
contador = 1

if numero > 0:
    while contador <= numero:
        print(f"Número: {contador}") 
        contador += 1
else:
    print("Tiene que poner un número positivo")

exit()
