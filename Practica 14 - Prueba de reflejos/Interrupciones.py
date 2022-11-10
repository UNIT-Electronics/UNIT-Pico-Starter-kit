#Definimos librerias
from machine import Pin
import time
#Librería que genera números aleatorios:
import random
#Definimos un puerto de entrada y uno de salida
led = Pin(2, Pin.OUT)
boton = Pin(3, Pin.IN, Pin.PULL_DOWN)
#Función Callback si se activa la interrupción:
def control_boton(pin):
    #Desactivamos la interrupción:
    boton.irq(handler=None)
    #Función que calcula el tiempo transcurrido entre ambas variables:
    timer_reaction = time.ticks_diff(time.ticks_ms(), timer_start)
    #Imprimimos el tiempo de reacción transcurrido
    print("Tiempo de reacción: " + str(timer_reaction) + " milisegundos")
        
print("\nIniciamos!!!")
#Encendemos el led, señal de que inicia el juego
led.value(1)
#Usamos la función random para generar un retardo indeterminado
time.sleep(random.uniform(5, 10))
print("\n¡Presiona ahora!")
#Apagamos el led, señal de que presiones el botón
led.value(0)
#Guardamos el tiempo en que se apago el led
#será nuestro tiempo inicial  de la prueba
timer_start = time.ticks_ms()
#Llamamos a la interrupción 
boton.irq(trigger=Pin.IRQ_RISING, handler=control_boton)
"""
Para correr de nueva cuenta el programa presiona el botón de "Stop"
y vuelve a ejecutar el script
"""