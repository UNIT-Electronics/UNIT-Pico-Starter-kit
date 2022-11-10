#Declaramos librerias
from machine import Pin
#Declaramos el pin de entrada que dará lectura al sensor, es un pin Pull Down
#porque el sensor entrega un voltaje activo de 3.3V
sensor_pir = Pin(2, Pin.IN, Pin.PULL_DOWN)

#Interrupción que se ejecutará cuando el sensor se active
def pir_interrupcion(pin):
    #Imprimimos mensaje
    print("Presencia detectada")
#Declaramos la interrupción del Pin sensor_PIR
sensor_pir.irq(trigger = Pin.IRQ_RISING, handler = pir_interrupcion)