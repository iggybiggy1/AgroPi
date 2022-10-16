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


def light_value():
    light_volt = light_chan.voltage
    light_perc = 30.303*(3.3 - light_volt)
    return round(light_perc,3)

def soil_moist():
    soil_volt = soil_chan.voltage
    soil_perc = 30.303*(3.3 - soil_volt)
    return round(soil_perc, 3)
    