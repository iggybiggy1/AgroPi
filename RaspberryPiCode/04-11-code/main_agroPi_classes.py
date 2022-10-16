from ADC_sensors import light_value, soil_moist
from time import sleep
from temp_humid_sense import temp_humid
import board
import adafruit_am2320 as af_am2320
from time import sleep
from datetime import datetime
from datetime import timedelta
import requests
import json
import os
import urllib.request


#i2c = board.I2C()
#am2320_sens = af_am2320.AM2320(i2c)
dict_strings = ["soil_moisture", "UV_index", "air_humidity", "air_temperature"]
global sensor_data
sensor_data = []
global ev_list
ev_list = []
post_bool = True
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


class sensor_readings(object):

    def __init__(self, time):
        self.time = time
        self.data = None
    def execute(self):
        t_now = datetime.now()
        while t_now < self.time:
            sleep(1)
            t_now = datetime.now()
        self.gather_data()
        self.store_data()

    def gather_data(self):
        data_point = []
        sleep(1)
        data_point.append(soil_moist())
        sleep(2)
        data_point.append(light_value())
        sleep(1)
        h_t_val = temp_humid()
        for i in range(2):
            data_point.append(h_t_val[i])
        self.data = data_point

    def store_data(self):
        sensor_data.append(self.data)
        print("sensor data: ")
        print(sensor_data)

class post_data(object):
    def __init__(self, time):
        self.time = time
        self.dict = None
    def execute(self):
        t_now = datetime.now()
        while t_now < self.time:
            sleep(1)
            t_now = datetime.now()
        self.dict_data(sensor_data)
        self.post()



    def post(self):
        print("posting here")
        if post_bool:
            url = 'https://agropiproject.herokuapp.com/data_point/'
            json_data = json.dumps(self.dict, default=str)
            req = urllib.request.Request(url)
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            print(datetime.now())
            print(json_data)
            jsondataasbytes = json_data.encode('utf-8')
            req.add_header('Content-Length', len(jsondataasbytes))
            response = urllib.request.urlopen(req, jsondataasbytes)


    def dict_data(self, data_list):
        ret_dict = {}
        ret_dict["timestamp"] = datetime.now()
        ret_dict["plant"] = plant_id
        num_data_points = len(data_list)
        for i in range(4):
            data_sum = 0
            for j in range(num_data_points):
                data_sum += data_list[j][i]
            avg_val = data_sum / num_data_points
            ret_dict[dict_strings[i]] = round(avg_val, 3)
        self.dict = ret_dict
        print("avg vals dict: ")
        print(self.dict)

class populate_ev(object):

    def __init__(self, time):
        self.time = time
    def execute(self):
        t_now = datetime.now()
        while t_now < self.time:
            sleep(1)
            t_now = datetime.now()

        print("populate evs")
        day_ = self.time.day
        hour_ = self.time.hour
        mins = self.time.minute
        mins += 1
        if (hour_ == 23 and mins >= 60):
            mins = 0
            hour = 0
        
        if (mins >= 60 and hour_ < 23):
            mins = 0
            hour_ += 1
        else:
            pass
        end_time = datetime(year=2021, month=11, day=day_, hour=hour_, minute=mins)
        self.create_pop(end_time)
        self.create_post(end_time)
        self.create_read(end_time)
    def create_read(self, t):
        min_15s = timedelta(seconds=15)
        ev_list.append(sensor_readings(t))
        new_time = t
        while new_time >= datetime.now():
            new_time = new_time - min_15s
            ev_list.append(sensor_readings(new_time))


    def create_post(self, t):
        ev_list.append(post_data(t))

    def create_pop(self, t):
        ev_list.append(populate_ev(t))

def main_func():

    ev_list.append(populate_ev(datetime.now()))
    while True:
        print(ev_list)
        curr_ev = ev_list.pop(-1)
        curr_ev.execute()
        sleep(1)






main_func()

