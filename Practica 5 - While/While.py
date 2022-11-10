contraseña = 123456 #Definimos la contraseña
#Solicitamos al usuario ingrese la contraseña
usuario = int(input ("Ingresa la contraseña "))
#Mientras la contraseña sea incorrecta se ejecutará el siguiente código
while usuario != contraseña:
    #Informamos que la contraseña es incorrecta
    print("¡Contraseña incorrecta!")
    #Solicitamos nuevamente la contraseña
    usuario = int(input("Ingresa la contraseña "))
#Cuando la contraseña sea correcta permitios el acceso
print("Acceso permitido")