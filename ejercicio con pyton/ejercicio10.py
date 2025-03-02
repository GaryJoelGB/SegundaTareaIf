#Clasificación de ángulos 
# Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).

valorAngulo = int(input("Digite el valor de un angulo:"))

if valorAngulo < 90:
    print("El ángulo es agudo (< 90°)")
elif valorAngulo == 90:
    print("El ángulo es recto (90°)")

elif 90 < valorAngulo < 180:
    print("El ángulo es obtuso (> 90° y < 180°)")

elif valorAngulo == 180:
    print("El ángulo es llano (180°)")

else:
    print(" digite un numero correcto del angulo")