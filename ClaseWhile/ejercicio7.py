#Escribe un programa que pida al usuario un número entero positivo y 
#luego imprima todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.

numero = int(input("Escribe un numero positivo:"))

if numero <= 0:
    print("ERROR, Tiene que poner un numero positivo")
else:
    i = 1
    while i <= numero:        
        print(i)
        i += 2 

