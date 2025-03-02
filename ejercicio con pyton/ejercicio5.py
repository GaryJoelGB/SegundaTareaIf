#Descuento por edad Un cine ofrece un descuento del 50% a personas mayores de 60 años. Solicita la edad del usuario y determina si aplica para el descuento.

edad = int(input("Escriba su edad para aplicar el descuento:"))

if edad >= 60:
    print ("Si aplica para el 50% del descuento")
elif edad < 18:
    print("Vete a dormir muchacho")

else:
    print("Eres mayor de edad pero no aplica para el descuento")

