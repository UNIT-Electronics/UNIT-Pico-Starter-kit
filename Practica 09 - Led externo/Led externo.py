#Definimos librerias
from machine import Pin
import time
#"led" se le asigna las propiedades del Pin 0 como salida
led = Pin(0, Pin.OUT)

while True: 
    #Esta línea de código manda un estado alto a la salida
    led.value(1)
    #Esta línea de de código ingresa un retardo de 1 segundo
    #antes de ejecutar la siguiente instrucción
    time.sleep(1)
    #Estado bajo a la salida
    led.value(0)
    #Retardo de 1 segundo
    time.sleep(1)
