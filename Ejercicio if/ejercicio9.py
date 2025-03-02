#Mayor entre tres números Pide al usuario tres números y muestra el mayor de ellos.

numero1 = int(input("Digite el numero 1:"))
numero2 = int(input("Digite el numero 2:"))
numero3 = int(input("Digite el numero 3:"))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero 1 es mayor {numero1}")

elif numero2 > numero1 and numero2 > numero3:
     print(f"El numero 2 es mayor {numero2}")
    
elif numero3 > numero1 and numero3 > numero2:
     print(f"El numero 3 es mayor {numero3}")