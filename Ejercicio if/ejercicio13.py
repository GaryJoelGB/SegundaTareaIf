#Verificación de año bisiesto
# Solicita al usuario un año y determina si es bisiesto o no. (Es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por 400).

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
