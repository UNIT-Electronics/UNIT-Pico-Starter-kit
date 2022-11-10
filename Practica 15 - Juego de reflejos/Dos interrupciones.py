#Definimos librerias
from machine import Pin
#Definimos nuestras entradas y salida, las entradas estan configuradas como Pull Down
boton_derecho = Pin(21, Pin.IN, Pin.PULL_DOWN)
boton_izquierdo = Pin(22, Pin.IN, Pin.PULL_DOWN)

#Función callback para activar la interrupción:
def funcion_interrupcion_izq(pin):
    #Desactivamos interrupción 1
    boton_izquierdo.irq(handler=None)
    print("Izquierda")

def funcion_interrupcion_der(pin):
    #Desactivamos interrupción 2
    boton_derecho.irq(handler=None)
    print("Derecha")

#Definimos las 2 interrupciones del programa, cada interrupción llama a una función distinta
#Se definen como flancos de subida
boton_izquierdo.irq(trigger = Pin.IRQ_RISING, handler= funcion_interrupcion_izq)

boton_derecho.irq(trigger = Pin.IRQ_RISING, handler= funcion_interrupcion_der)