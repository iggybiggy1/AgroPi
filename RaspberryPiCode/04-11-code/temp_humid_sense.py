import board
import adafruit_am2320 as af_am2320
from time import sleep
i2c = board.I2C()
am2320_sens = af_am2320.AM2320(i2c)


def temp_humid():
    while True:
        try:
           humidity = am2320_sens.relative_humidity
           break
        except:
            pass
            
    while True:
        try:
           temp = am2320_sens.temperature
           break
        except:
            pass
    return [humidity, temp]
