#Añadiremos la nueva libreria ADC
from machine import Pin, ADC
import time
#Asignaremos a Potenciometro la lectura ADC del pin 26
potenciometro = ADC(26)
#Constante de conversion de ADC a Voltaje
conversion_factor = 3.3 / (65535)

while True:
    #¿Cuantos bits obtienes de lectura?
    print("\nValor en bits: ", potenciometro.read_u16())
    #Ecuacion para obtener la lectura de voltaje
    voltaje = potenciometro.read_u16() * conversion_factor
    #Imprimimos el voltaje leido en la consola
    print("Valor en volts: ", voltaje)
    #Cada 0.5s se realizará una nueva lectura
    time.sleep(0.5)