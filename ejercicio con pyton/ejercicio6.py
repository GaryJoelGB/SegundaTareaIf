#Calificación aprobatoria  Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobo.

calificacion = int(input("Escriba su calificacion de 0 al 100:"))

if calificacion >= 60 and calificacion <= 100:
    print("aprobo")

elif calificacion <= 59:
    print ("Reprobo por burro")

else:
    print("Pon el numero correcto.")
