#Cálculo de impuestos
# Pide al usuario su salario mensual y aplica los siguientes impuestos:
# Menos de 10,000: 0%
# Entre 10,000 y 30,000: 10%
# Más de 30,000: 20%

salario = float(input("Digite su salario:"))


if salario < 10000 and salario > 0:
    print(f"No  tiene impuesto tu salario es:{salario}")

elif salario >= 10000 and salario <= 30000:
        
        impuesto = salario * 0.10

        salarioImpuesto =  salario - impuesto

        print(f"Tu impuesto del 10% es {impuesto} y tu salario restante es: {salarioImpuesto}")
elif salario > 30000:
        
        impuesto = salario * 0.20

        salarioImpuesto = salario - impuesto
        print(f"Tu impuesto del 20% es {impuesto} colocado y tu salario restante es: {salarioImpuesto}")

else:
       print("tu salario minimo debe ser de 1")