from ADC_sensors import light_value, soil_moist
from time import sleep
from temp_humid_sense import temp_humid
import board
import adafruit_am2320 as af_am2320
from time import sleep
from datetime import datetime
import requests
import json
import os
import urllib.request


#i2c = board.I2C()
#am2320_sens = af_am2320.AM2320(i2c)
dict_strings = ["soil_moisture", "UV_index", "air_humidity", "air_temperature"]
sensor_data = []

try:
    plant_txt = open("plantid.txt", "r")
    if os.stat("plantid.txt").st_size == 0:
        raise Exception("file empty")
    plant_id = plant_txt.read()
    print(plant_id)
except:
    print("requesting plant id....")
    plant_id_req = requests.get(url = 'https://agropiproject.herokuapp.com/register_pi')
    request_dec = plant_id_req.json()
    print(request_dec['plant_id'])
    id_txt = open("plantid.txt", "w")
    id_txt.write(str(request_dec['plant_id']))
    id_txt.close()
    

def sensor_readings():
    data_point = []
    sleep(1)
    data_point.append(soil_moist())
    sleep(2)
    data_point.append(light_value())
    sleep(1)
    h_t_val = temp_humid()
    for i in range(2):
        data_point.append(h_t_val[i])
    
    return data_point
    
def dict_data(data_list):
    ret_dict = {}
    ret_dict["timestamp"] = datetime.now()
    ret_dict["plant"] = plant_id
    num_data_points = len(data_list)
    for i in range(4):
        data_sum = 0
        for j in range(num_data_points):
            data_sum += data_list[j][i]
        avg_val = data_sum / num_data_points
        ret_dict[dict_strings[i]] = round(avg_val,3)
    return ret_dict
            
def post_data(in_dict):
    url = 'https://agropiproject.herokuapp.com/data_point/'
    json_data = json.dumps(in_dict, default=str)
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    print(datetime.now())
    print(json_data)
    jsondataasbytes = json_data.encode('utf-8')
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)


def main_func():
    
    
    #AUTOMATION
    
    return 0
    
    
    
sensor_data.append(sensor_readings())
print(sensor_data)

test_dict = dict_data(sensor_data)
post_data(test_dict)

