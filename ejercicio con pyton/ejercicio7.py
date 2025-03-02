#Día de la semana Escribe un programa que solicite un número del 1 al 7 y muestre el día de la semana correspondiente (1 es lunes, 7 es domingo).

numero = int(input("Escribe un numero del 1 al 7:"))

if numero == 1:
    print("Lunes")

elif numero == 2:
    print("Martes")

elif numero == 3:
    print("Miercoles")

elif numero == 4:
    print("Jueves")

elif numero == 5:
    print("Viernes")

elif numero == 6:
    print("Sabado")

elif numero == 7:
    print("Domingo")
else:
    print("No pusiste un numero del 1 al 7")
