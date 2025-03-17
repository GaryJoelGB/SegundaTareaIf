#Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. 
# El programa debe continuar hasta que el usuario ingrese la contraseña correcta. 
# Utiliza una estructura whilepara simular un do while.

contra = "gary97"

while True:
    seguridad = input("Ingrese la contraseña: ")
    
    if seguridad == contra:

        print(" Acceso permitido.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")
exit()