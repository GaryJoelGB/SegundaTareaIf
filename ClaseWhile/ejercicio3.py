#Escribe un programa que pida al usuario un número entero positivo.
# El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.

numero = int(input("Escriba un numero entero positivo:"))
if numero < 0:
    print(" Error, tiene que poner un numero positivo.")
else:
    contador = 0
    temporal = numero

while temporal > 0:
    temporal //= 10
    contador += 1

    print(f"El numero {numero} tiene contador {contador} digitos")    
