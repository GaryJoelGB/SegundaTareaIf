#Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. 
#El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.

numero = int(input("Ingrese un numero positivo:"))

if numero <= 0:
    print("Error, escribe un numero positivo")

else:
    factorial = 1
    i = 1
    while i < numero:
        factorial *= i
        i +=1
        print(factorial)

exit()