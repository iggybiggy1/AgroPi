import board
import adafruit_am2320 as af_am2320

#make sure adafruit package is installed, and I2C is enabled on Pi

i2c = board.I2C()
am2320_sens = af_am2320.AM2320(i2c)
humid_air = am2320_sens.relative_humidity
temp_air = am2320_sens.temperature

print(humid_air)
print(temp_air)