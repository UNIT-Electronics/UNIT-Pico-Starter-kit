#Definimos librerias
from machine import Pin
import time
"""
"button" se le asigna las propiedades del Pin 0,1,2,3,etc
Pin.In se declara como un pin de entrada
Pin.PULL_DOWN declara que esa entrada funcione como una resistencia
Pull Down
Pin.PULL_UP declara que esa entrada funcione como una resistencia
Pull Up
"""
button1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    #En Pull Down el pin se activa con un 1 lógico
    if button1.value() == 1: 
        print("¡Presionaste el boton 1!")
        #Ingresamos un retardo de 0.5 segundos
        time.sleep(0.5)
    #En Pull Up el pin detecta el interruptor con un 0 lógico 
    if button2.value() == 0:
        print("¡Presionaste el boton 2!")
        #Ingresamos un retardo de 0.5 segundos
        time.sleep(0.5)
        