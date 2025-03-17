#Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, 
#el valor de n lo ingresa el usuario, utilizando un bucle for.

numero = int(input("Ingrese el numero de termino de la serie fibonacci:"))

if numero <= 0:
    print("Error, ingrese un numero positivo")

else:
    a,b = 0,1
    for _ in range(numero):
        print(a,end="")
        a,b = b, a+b
exit()