#Clasificación de números
#  Pide al usuario tres números y determina si son todos positivos, todos negativos, mixtos o si hay ceros.

numero1 = int(input("Digite el 1 numero:"))
numero2 = int(input("Digite el 2 numero:"))
numero3 = int(input("Digite el 3 numero:"))

if numero1 > 0 and numero2 > 0 and numero3 > 0:
    print("Todos los numero son positivo")
elif numero1 < 0 and numero2 < 0 and numero3 < 0:
    print("Todos los numero son negativo")
else:
    print("Son numero mixtos o hay ceros")