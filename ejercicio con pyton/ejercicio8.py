#Número mayor entre dos  Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales.

numero1 = int(input("Digite un numero:"))
numero2 = int(input("Digite el numero 2:"))

if numero1 > numero2:
    print(f"Tu primer numero es mayor que el segundo numero:{numero1}")
elif numero2 > numero1:
    print(f"Tu segundo numero es mayor que el primer numero:{numero2}")
else:
    print("Son iguales")


