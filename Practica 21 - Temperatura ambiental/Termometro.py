#Añadiremos la nueva libreria ADC
from machine import Pin, ADC
import time
#Asignaremos a sensor_temp la lectura ADC del canal 4
sensor_temp = ADC(4)
#Constante de conversion de ADC a Voltaje
conversion_factor = 3.3 / (65535)

while True:
    #Ecuacion para obtener la lectura de voltaje
    lectura = sensor_temp.read_u16() * conversion_factor
    #Ecuación para convertir el voltaje en temperatura
    temperatura = 27 - (lectura - 0.706)/0.001721
    #Imprimimos en consola la temperatura
    print("\nTemperatura ambiente: ", temperatura, " °C")
    #Cada 2s se realizará una nueva lectura
    time.sleep(2)