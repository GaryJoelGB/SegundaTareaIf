#Comparación de tres longitudes
#  Solicita tres números que representan longitudes y determina si pueden formar un triángulo (la suma de dos lados debe ser mayor que el tercero).


lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Las longitudes pueden formar un triángulo.")
else:
    print("Las longitudes no pueden formar un triángulo.")
