import glob
import time
import os
import sys


w1_addtag = "/sys/bus/w1/devices/"

def temp_sens_readings():
    rtn = {}
    w1_devices = []
    w1_devices = os.listdir(w1_addtag)
    
    #only set up for when there is one w1 device
    deviceid = w1_devices[1]
    reading_path = w1_addtag + deviceid + "/w1_slave"
    rtn[deviceid] = {}
    rtn[deviceid]['temp_c'] = None
    
    if os.path.isfile(reading_path):
        try:
            file = open(reading_path, "r")
            data_read = file.read()
            file.close()
            if "YES" in data_read:
                (disc, sep, val) = data_read.partition(' t=')
                #store and adjust value
                rtn[deviceid]['temp_c'] = float(val)/float(1000.0)
            else:
                rtn[deviceid]['error'] = 'No YES in data: bad data.'
        except Exception as e:
            rtn[deviceid]['error'] = 'Exception parsing data file: ' + str(e)
    else:
        rtn[deviceid]['error'] = 'w1_slave data not found'
    return rtn


                
for t in range(10):
    curr_rtn = temp_sens_readings()
    for dev_id in curr_rtn:
        if not 'error' in curr_rtn[dev_id]:
            print("dev id: " + dev_id + " time: " + str(time.time()) \
                  + " read: " + str(curr_rtn[dev_id]['temp_c']))
    time.sleep(5.0)

# w1_devices = []
#w1_devices = os.listdir("/sys/bus/w1/devices/")
#print(type(w1_devices[1]))
