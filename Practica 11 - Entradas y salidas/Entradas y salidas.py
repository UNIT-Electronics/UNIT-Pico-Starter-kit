#Definimos librerias
from machine import Pin
import time
#"led" se le asigna las propiedades del Pin 21 como salida
led = Pin(21, Pin.OUT)
#"button" se le asignan las propiedades del Pin 22 como entrada conectada a un resistor Pull Down
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
    #En Pull Down el pin se activa con un 1 lógico
    if button.value() == 1: 
        led.value(1)
        #Ingresamos un retardo de 2 segundos despues de presionar el led
        time.sleep(2)
    #Al dejar de presionar el boton el led se apaga
    led.value(0)