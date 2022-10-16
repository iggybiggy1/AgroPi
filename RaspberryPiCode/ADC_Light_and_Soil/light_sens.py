import busio
import digitalio
import board

from time import sleep
import adafruit_mcp3xxx.mcp3004 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

#chip select
cs = digitalio.DigitalInOut(board.D5)

#mcp object
mcp = MCP.MCP3004(spi, cs)

#analog light channel
light_chan = AnalogIn(mcp, MCP.P0)
soil_chan = AnalogIn(mcp, MCP.P3)

while True:
    print('-------------------')
    print("Raw ADC value Light: " +str(light_chan.value))
    print('Light Voltage: ' +str(light_chan.voltage)+'V')
    sleep(0.5)
    print("Raw ADC soil: " + str(soil_chan.value))
    print('Soil Voltage: '+ str(soil_chan.voltage)+'V')
    sleep(4)





