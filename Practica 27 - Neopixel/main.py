import time
#Libreria para utilizar la Neopixel
from neopixel import Neopixel
#Variables de configuración
NUM_LEDS  = 24	#¿Cuantos leds tiene tu tira?
LED_PIN = 2		#Pin de conexión
#Declaramos el objeto con propiedades de Neopixel
pixels = Neopixel(NUM_LEDS , 0, LED_PIN, "GRB")

velocidad = 0.1 	#Cambio de pixel, en segundos
brillo = 10#Brillo del led, 1 a 255
#Definimos colores
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
#Cadena donde se almacenan los colores
colors_rgb = (red, orange, yellow, green, blue, indigo, violet)
#Brillo del led
pixels.brightness(brillo)
#Ciclo de trabajo
"""
while True:
    #Este ciclo cambia de color
    for color in colors_rgb:
        #Este ciclo cambia de pixel
        for i in range(NUM_LEDS ):
            #Definimos el led y el color que deseamos
            pixels.set_pixel(i, color)
            #Retardo 
            time.sleep(velocidad)
            #Mandamos a la tira led el comando
            pixels.show()
"""
white = (255, 255, 255)
brown = (111, 78, 55)
while True:
    pixels.set_pixel(0, red)
    pixels.set_pixel(1, red)
    pixels.set_pixel(2, red)
    pixels.set_pixel(3, white)
    pixels.set_pixel(4, white)
    pixels.set_pixel(5, white)
    pixels.set_pixel(6, green)
    pixels.set_pixel(7, green)
    pixels.set_pixel(8, red)
    pixels.set_pixel(9, red)
    pixels.set_pixel(10, red)
    pixels.set_pixel(11, white)
    pixels.set_pixel(12, brown)
    pixels.set_pixel(13, white)
    pixels.set_pixel(14, green)
    pixels.set_pixel(15, green)
    pixels.set_pixel(16, red)
    pixels.set_pixel(17, red)
    pixels.set_pixel(18, red)
    pixels.set_pixel(19, white)
    pixels.set_pixel(20, white)
    pixels.set_pixel(21, white)
    pixels.set_pixel(22, green)
    pixels.set_pixel(23, green)
    pixels.show()
    time.sleep(0.3)
    pixels.set_pixel(0, red)
    pixels.set_pixel(1, red)
    pixels.set_pixel(2, white)
    pixels.set_pixel(3, white)
    pixels.set_pixel(4, white)
    pixels.set_pixel(5, green)
    pixels.set_pixel(6, green)
    pixels.set_pixel(7, green)
    pixels.set_pixel(8, red)
    pixels.set_pixel(9, red)
    pixels.set_pixel(10, white)
    pixels.set_pixel(11, brown)
    pixels.set_pixel(12, white)
    pixels.set_pixel(13, green)
    pixels.set_pixel(14, green)
    pixels.set_pixel(15, green)
    pixels.set_pixel(16, red)
    pixels.set_pixel(17, red)
    pixels.set_pixel(18, white)
    pixels.set_pixel(19, white)
    pixels.set_pixel(20, white)
    pixels.set_pixel(21, green)
    pixels.set_pixel(22, green)
    pixels.set_pixel(23, green)
    pixels.show()
    time.sleep(0.3)
