#Definimos librerias
from machine import Pin
from time import sleep, ticks_ms
import random
#Definimos nuestras entradas y salida, las entradas estan configuradas como Pull Down
led = Pin(20, Pin.OUT)
boton_derecho = Pin(21, Pin.IN, Pin.PULL_DOWN)
boton_izquierdo = Pin(22, Pin.IN, Pin.PULL_DOWN)
#Variable de apoyo para saber quien presiono el botón
boton_presionado = None
#Función callback para activar la interrupción:
def funcion_interrupcion(pin):
    #Desactivamos interrupción 1
    boton_derecho.irq(handler=None)
    #Desactivamos interrupción 2
    boton_izquierdo.irq(handler=None)
    #Definimos la variable como global para poder modificarla
    global boton_presionado
    #La variable "boton_presionado" almacenará el valor del pin donde se produjo primero la interrupción
    boton_presionado = pin

print("\nIniciamos!!!")
#Encendemos el led, señal de que inicia el juego
led.value(1)
#Usamos la función random para generar un retardo indeterminado
sleep(random.uniform(5, 10))
print("\n¡Presiona ahora!")
#Apagamos el led, señal de que presiones el botón
led.value(0)
#Definimos las 2 interrupciones del programa, ambasa interrupciones llevarán a la misma función
#Se definen como flancos de subida
boton_izquierdo.irq(trigger = Pin.IRQ_RISING, handler= funcion_interrupcion)
boton_derecho.irq(trigger = Pin.IRQ_RISING, handler= funcion_interrupcion)

#Mientras esperamos a que una de las interrupciones se dispare no hacemos nada
while boton_presionado is None:
    sleep (1)

#Si la interrupción es por Boton Derecho se imprime en la consola al ganador
if boton_presionado is boton_derecho:
    print("Felicidades: Jugador DERECHO")

#Si la interrupción es por Boton Izquierdo se imprime en la consola al ganador
elif boton_presionado is boton_izquierdo:
    print("Felicidades: Jugador IZQUIERDO")