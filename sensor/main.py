import dht
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime
from machine import Pin

  
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #i'm using LCD screen to show temp 
utime.sleep_ms(100)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
sensor = dht.DHT11(Pin(14))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    print(temp)
    lcd.clear()
    lcd.putstr('Temp: {}C\nHum: {}%'.format(temp, hum))
    utime.sleep(2)
    lcd.clear()
    
    time = utime.localtime()
    lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
    year=time[0], month=time[1], day=time[2],
    HH=time[3], MM=time[4], SS=time[5]))
    utime.sleep(2)
    
 