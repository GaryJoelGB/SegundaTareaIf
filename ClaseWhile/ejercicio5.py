#Escribe un programa que pida al usuario un número entero y 
#luego imprima todos los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.

numero = int(input("Escribe un numero:"))
for i in range(numero,-1,-1):
    print(i)