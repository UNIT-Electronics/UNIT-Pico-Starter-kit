#Declaramos librerias
from machine import Pin
import time
#Definimos el pin de entrada para el sensor
sensor_pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
#Pin de salida para el led
led = Pin(17, Pin.OUT)
#Valor inicial del led
led.value(0)
#Interrupción que se ejecutará cuando el sensor se active
def pir_handler(pin): 
    print("Presencia detectada")
    #Ciclo For para hacer parpadear el led, se repite 50 veces
    for i in range (50):
        #Instrucción para cambiar el estado del led
        led.toggle()
        #Intrucción para pausar 100mS la compilación del código
        time.sleep_ms(100)
#Activamos la interrupción      
sensor_pir.irq(trigger = Pin.IRQ_RISING, handler=  pir_handler)
#Menú principal
while True:
    #Instrucción para cambiar el estado del led
    led.toggle()
    time.sleep(2)