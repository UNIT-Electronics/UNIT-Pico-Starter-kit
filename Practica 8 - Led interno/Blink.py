#Definimos librerias
from machine import Pin
import time
#"led" se le asigna las propiedades del Pin 25 como salida
led = Pin(25, Pin.OUT)

while True:
    #Esta línea de código manda un estado alto a la salida
    led.value(1)
    #Esta línea de de código ingresa un retardo de 1 segundo
    #antes de ejecutar la siguiente instrucción
    time.sleep(1)
    #Estado bajo a la salida
    led.value(0)
    #Retardo de 0.5 segundos
    time.sleep(0.5)