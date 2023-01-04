#Añadiremos la nueva libreria PWM
from machine import Pin, PWM
import time
#Al objeto 'led' le asignamos las propiedades de PWM
#Se declara al pin 2 como salida PWM
led = PWM(Pin(2))
#Frecuencia de trabajo
led.freq(1000)

while True:
    #Ciclo para aumentar poco a poco el brillo del led
    for i in range (0,65536,10):
        #Asignamos al ciclo util el valor de i
        led.duty_u16(i)
        #Retardo de 1 milisegundos
        time.sleep(0.001)
    #Retardo de 2 segundos
    time.sleep(2)