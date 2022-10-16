from gpiozero import DigitalInputDevice
from time import sleep


light_sens = DigitalInputDevice(17, bounce_time=1)
soil_moist = DigitalInputDevice(27, bounce_time=1)

for i in range(7):
    if light_sens.value == 0
        print("Lights are on")
    else:
        print("lights are off")
    
    if soil_moist.value == 0
        print("Soil is moist")
    else:
        print("soil is not moist")
    sleep(5)
    
