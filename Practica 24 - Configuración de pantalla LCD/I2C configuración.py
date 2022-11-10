#Definimos librerias Pin, I2C y tiempo
from machine import Pin, I2C
import time
#Definimos pines para I2C
sda_pin = Pin(6)
scl_pin = Pin (7)
#Configuramos los pines para I2C
i2c = I2C(1, sda = sda_pin, scl = scl_pin, freq = 400000)

try:
    direccion = hex(i2c.scan()[0])
    print("La dirección I2C de la LCD es: ", direccion)
except:
    print("Dispositivo no encontrado, revisa tus conexiones y voltajes")