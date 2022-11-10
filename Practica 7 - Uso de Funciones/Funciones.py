#La palabra "def" se utiliza para declarar una función
def Calculadora (x,y):
#Los valores entre parentesis son las variables con las que trabaja la función
    #Suma
    z = x + y
    print("\nSuma: ")
    print( x, " + ", y," = ", z)

    #Resta
    z = x - y
    print("Resta: ")
    print( x, " - ", y," = ", z)

    #Multiplicación
    z = x * y
    print("Multiplicación: ")
    print( x, " * ", y," = ", z)

    #División
    z = x / y
    print("División: ")
    print( x, " / ", y," = ", z)

    #División sin número decimal
    z = x // y
    print("División sin número decimal: ")
    print( x, " // ", y," = ", z)

    #Potencia
    z = x ** y
    print("Potencia: ")
    print( x, " ^ ", y," = ", z)

#Ciclo indefinido
while True:
    #Ingresa los dos números a utilizar
    x = int (input("\nIngresa el primer número "))
    #Utilizar el caracter \n grega un espacio entre renglones
    y = int (input("Ingresa el segundo número "))
    Calculadora (x,y)