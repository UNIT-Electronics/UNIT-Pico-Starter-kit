#Definimos librerias
from machine import Pin
import time
#Declaramos los 3 pines que vamos utilizar como salidas
#Un pin por cada color del semaforo
led_verde = Pin(13, Pin.OUT)
led_amarillo = Pin(14, Pin.OUT)
led_rojo = Pin(15, Pin.OUT)
#Declaramos los valores inicales de cada salida
#En este caso se inicia en 0 para evitar que se inicien todos encendidos
led_rojo.value(0)
led_amarillo.value(0)
led_verde.value(0)

while True:
    #Luz roja por 5 segundos, verde y amarillo apagadas 
    led_rojo.value(1) 
    time.sleep(5) 
    #Verde encendido por 5 segundos, rojo y amarillo apagado
    led_rojo.value(0) 
    led_amarillo.value(0) 
    led_verde.value(1)
    time.sleep(5)
    #Amarillo encendido por 2 segundos, verde y rojo apagado
    led_verde.value(0) 
    led_amarillo.value(1) 
    time.sleep(2)
    #Apagamos la luz amarilla para reiniciar el ciclo
    led_amarillo.value(0)