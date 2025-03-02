#Clasificación de IMC
# Solicita el peso (kg) y la altura (m) de una persona, calcula su Índice de Masa Corporal (IMC = peso / altura²) y clasifícalo:
#<18.5: Bajo peso
#18.5-24.9: Normal
#25-29.9: Sobrepeso
#30 o más: Obesidad

peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Tu IMC es {imc:.2f}. Bajo peso.")
elif 18.5 <= imc <= 24.9:
    print(f"Tu IMC es {imc:.2f}. Normal.")
elif 25 <= imc <= 29.9:
    print(f"Tu IMC es {imc:.2f}. Sobrepeso.")
else:
    print(f"Tu IMC es {imc:.2f}. Obesidad.")
