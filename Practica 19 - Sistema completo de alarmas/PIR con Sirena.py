#Importamos librerias
from machine import Pin
import time
#Definimos el pin de entrada para el sensor
sensor_pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
#Definimos pines de salida
led = Pin(17, Pin.OUT)
buzzer = Pin(18, Pin.OUT)
##Interrupción que se ejecutará cuando el sensor se active
def interrupcion_PIR (pin):
    print("Presencia detectada")
    #Ciclo para prender y apagar rapidamente el led
    for i in range (50):
        #Instrucción que cambia de estado el pin del Led
        led.toggle()
        for j in range (25):
            #Instrucción que cambia de estado el pin del Buzzer
            buzzer.toggle()
            #Retardo de 3 mili segundos
            time.sleep_ms(3)
            
#Declaramos la interrupción del Pin sensor_PIR
sensor_pir.irq(trigger = Pin.IRQ_RISING, handler = interrupcion_PIR)

while True:
    #Mientras se activa la interrupción el led parpadeará cada 2 segundos
    led.toggle()
    time.sleep(2)