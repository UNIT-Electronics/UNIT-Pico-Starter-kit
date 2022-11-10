#Definimos librerias
from machine import Pin, I2C
from time import sleep
import random
#Librerias necesarias para utilizar la LCD:
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
#Definimos nuestras entradas y salidas
led = Pin(20, Pin.OUT)
sda_pin = Pin(6)
scl_pin = Pin (7)
boton_derecho = Pin(21, Pin.IN, Pin.PULL_DOWN)
boton_izquierdo = Pin(22, Pin.IN, Pin.PULL_DOWN)
#Configuramos los pines para I2C
i2c = I2C(1, sda = sda_pin, scl = scl_pin, freq=400000)
#Obtenemos la dirección I2C de la LCD
I2C_DIREC = i2c.scan()[0]
#Definimos el tipo de LCD que ocuparemos
#Si ocupas un LCD de otras dimensiones, aqui debes de modificarlas
I2C_FILAS = 2
I2C_COLS = 16
#Configuramos la LCD con las bibliotecas que descargamos
lcd = I2cLcd (i2c, I2C_DIREC, I2C_FILAS, I2C_COLS)
#Variable de apoyo para saber quien presiono el botón
boton_presionado = None
#Función callback para activar la interrupción:
def funcion_interrupcion(pin):
    #Desactivamos interrupción 1
    boton_derecho.irq(handler=None)
    #Desactivamos interrupción 2
    boton_izquierdo.irq(handler=None)
    #Variable global para boton
    global boton_presionado
    #Obtenemos el pin de la primera interrupción
    boton_presionado = pin
    #Ciclo para prender y apagar la pantalla
    for i in range(6):
        # Apaga la luz de fondo de la pantalla
        lcd.backlight_off()
        sleep(0.1)
        # Enciende la luz de fondo de la pantalla
        lcd.backlight_on()
        sleep(0.1)
#Ciclo indeterminado de juegos
while True:
    #Limpiamos pantalla
    lcd.clear()
    #Inicia la pantalla en Col: 2, Fila: 0
    lcd.move_to(2, 0)
    lcd.putstr("Iniciamos!!!")
    #Encendemos el led, señal de que inicia el juego
    led.value(1)
    #Usamos la función random para generar un retardo indeterminado
    sleep(random.uniform(5, 10))
    #Limpiamos pantalla
    lcd.clear()
    #Apagamos el led, señal de que presiones el botón
    led.value(0)
    lcd.putstr("Presiona ahora!")
    #Interrupciones del programa, se definen como flancos de subida
    boton_izquierdo.irq(trigger = Pin.IRQ_RISING, handler= funcion_interrupcion)
    boton_derecho.irq(trigger = Pin.IRQ_RISING, handler= funcion_interrupcion)
    #Mientras esperamos a que una de las interrupciones se dispare no hacemos nada
    while boton_presionado is None:
        sleep (1)

    lcd.clear()
    lcd.putstr("Ganador: Jugador")
    #Si la interrupción es por Boton Derecho se imprime en la consola al ganador
    if boton_presionado is boton_derecho:
        lcd.move_to(4, 1)
        lcd.putstr("DERECHO")
    #Si la interrupción es por Boton Izquierdo se imprime en la consola al ganador
    elif boton_presionado is boton_izquierdo:
        lcd.move_to(3, 1)
        lcd.putstr("IZQUIERDO")
        
    sleep(10)	#Esperamos 10 segundos a reiniciar el juego
    #Valor de boton para reiniciar el juego
    boton_presionado = None
