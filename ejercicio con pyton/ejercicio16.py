#Calculadora de descuentos
# Solicita el precio de un producto y aplica descuentos según el monto:
#Menos de $50: sin descuento
#Entre $50 y $100: 5%
#Más de $100: 10%
# Solicitar el precio del producto
precio = float(input("Ingrese el precio del producto: $"))

if precio < 50:
    descuento = 0  
elif 50 <= precio <= 100:
    descuento = 0.05 
else:
    descuento = 0.10  

precio_con_descuento = precio - (precio * descuento)

if descuento > 0:
    print(f"El precio con descuento es: ${precio_con_descuento:.2f}")
else:
    print(f"El precio no tiene descuento y es: ${precio:.2f}")
