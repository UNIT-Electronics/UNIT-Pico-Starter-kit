#Definimos librerias Pin, I2C y tiempo
from machine import I2C,Pin
import time
#Librerias necesarias para utilizar la LCD:
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
#Definimos pines para I2C
sda_pin = Pin(6)
scl_pin = Pin (7)
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

lcd.putstr("H")		#Imprimimos una letra
time.sleep(0.5)		#Retardo de 1/2 segundo

lcd.putstr("o")
time.sleep(0.5)

lcd.putstr("l")
time.sleep(0.5)

lcd.putstr("a")
time.sleep(0.5)
#Imprimimos caracteres, observa el espacio al inicio de la palabra
lcd.putstr(" mundo")
time.sleep(2)
#Ciclo para imprimir un conteo del 0 al 15
for i in range (0, 16):
    #Coordenada de inicio (columna, fila)
    lcd.move_to(7, 1)
    #Imprimimos el conteo, utilizando la funcion str()
    lcd.putstr(str(i))
    time.sleep(1)
    
#Borramos la pantalla
lcd.clear()