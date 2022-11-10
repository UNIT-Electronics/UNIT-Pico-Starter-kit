#Definimos librerias
from machine import Pin
import time
#Esta librería nos ayuda a utilizar los 2 nucleos de la Pi Pico
import _thread
#Declaramos los 4 pines que vamos utilizar como salidas
#Un pin por cada color del semaforo y otro para el buzzer
led_rojo = Pin(15, Pin.OUT)
led_amarillo = Pin(14, Pin.OUT)
led_verde = Pin(13, Pin.OUT)
buzzer = Pin(12, Pin.OUT)
#Declaramos nuestro pin de entrada
boton = Pin(16, Pin.IN, Pin.PULL_DOWN)
#Declaramos los valores inicales de cada salida
#En este caso se inicia en 0 para evitar que se inicien todos encendidos
led_rojo.value(0)
led_amarillo.value(0)
led_verde.value(0)
buzzer.value(0)
#Declaramos una variable global para que se ejecute en ambos nucleos
global boton_on
#valor inicial de variable global
boton_on = False
#Función que se ejecutará en el segundo hilo
def activacion_boton_thread():
    #Declaramos la variaable global para modificarla
    global boton_on
    #Ciclo infinito
    while True:
        # Si se presiona el boton, boton_on se marca como verdadero
        if boton.value() == 1: 
            boton_on = True
#Instrucción que declara que la función anterior se ejecutará en el segundo hilo de la Pi Pico          
_thread.start_new_thread(activacion_boton_thread, ())
#Ciclo infinito
while True:
    #Como solo queremos leer el valor de la variable no se vuelve a declarar 
    if boton_on == True:
        #Si el botón esta activado se ejecuta el sistema peatonal
        led_rojo.value(1)
        #Alarma auditiva
        for i in range(0, 12): 
            buzzer.value(1) 
            time.sleep(0.2) 
            buzzer.value(0) 
            time.sleep(0.2)
        #Modificamos la variable global para darle un valor falso
        global boton_on 
        boton_on = False
        #Cuando se presione el botón nuevamente  regresará el boton a Verdadero
        
    #Ciclo que ejecuta los colores del semaforo
    led_rojo.value(1) 
    time.sleep(5)

    led_rojo.value(0) 
    led_amarillo.value(0) 
    led_verde.value(1) 
    time.sleep(5)
    
    led_verde.value(0) 
    led_amarillo.value(1) 
    time.sleep(2) 
    led_amarillo.value(0)