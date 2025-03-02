#Conversión de calificaciones
# Solicita la calificación numérica de un estudiante (0-100) y conviértela en una letra:
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#0-59: F

numero = int(input("Digite su calificacion:"))

if numero >= 90 and numero <= 100:
    print("A")
elif numero >= 80 and numero <= 89:
    print("B")
elif numero >=70 and numero <=79:
    print("C")
elif numero >=60 and numero <=69:
    print("D")
elif numero >= 0 and numero <= 59:
    print("F")
else:
    print("Digite un numero por encima del 0 hasta el 100")