#Importamos librerias
from machine import Pin
import time
#Definimos el pin de entrada para el sensor
sensor_pir = Pin(2, Pin.IN, Pin.PULL_DOWN)
#Pin de salida para el relevador
rele = Pin(16, Pin.OUT)
#Valor inicial del relevador
rele.value(1)
"""
Funcionamiento del relevador:
1 -> Rele desactivado
0 -> Rele activado
"""
#Interrupción que se ejecutará cuando el sensor se active
def pir_interrupcion(pin): 
    print("Presencia detectada")
    rele.value(0)		#Activamos el relevador
    time.sleep(10)		#10 segundos de activación del rele
    rele.value(1)		#Apagamos el rele

#Declaramos la interrupción del Pin sensor_PIR
sensor_pir.irq(trigger = Pin.IRQ_RISING, handler=  pir_interrupcion)

while True:
    #Mientras se activa la interrupción el rele permanece desactivado
    rele.value(1)