
#Número positivo, negativo o cero
# Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero.

numero = int(input("Escribe un número:"))

if numero > 0:
    print("Tu numero es positivo")
elif numero == 0:
    print ("Tu numero es 0")

else:
    print ("Tu numero es negativo")
