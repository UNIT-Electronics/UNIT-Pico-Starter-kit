#Definimos librerias
from machine import Pin
import time
#"led" se le asigna las propiedades del Pin 0 como salida
led = Pin(0, Pin.OUT)

while True: 
    led.toggle() 
    time.sleep(2)