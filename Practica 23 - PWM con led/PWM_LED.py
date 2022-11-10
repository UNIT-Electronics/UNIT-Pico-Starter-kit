#Añadiremos la nueva libreria PWM, tambien utilizaremos ADC y Pin
from machine import Pin, ADC, PWM
import time
#Asignaremos a potenciometro la lectura ADC del pin 28
potenciometro = ADC(28)
#Led se le asignan las propiedades de PWM al Pin 2
led = PWM(Pin(2))
#Frecuencia de trabajo
led.freq(1000)

while True:
    #Ciclo util del PWM, es el valor del Potenciometro
    led.duty_u16(potenciometro.read_u16())