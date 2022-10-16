import pymongo
from time import sleep
from datetime import datetime

# connect
mongo_db = pymongo.MongoClient("mongodb+srv://agroPi:TTrqxQhMqAo2soUc@cluster0.fwswg.mongodb.net/agroPi?retryWrites=true&w=majority")

sleep(3)
print(mongo_db.admin.command('ping'))

# select db
agroPi_db = mongo_db.agroPi
sleep(1)
print(agroPi_db.list_collection_names())
print('-----------------------------')

# select collection
data_collection = agroPi_db['agroPi_datapoint']
sleep(1)
# test for finding a document
print(data_collection.find_one({'id': 2}))
id_2dp = data_collection.find_one({'id': 2})
print(id_2dp['air_temperature'])


# creates the dictionary to be inserted into collection
def rtn_data_dict(id_, air_t, air_h, uv_ind, soil_m, p_id, timestamp):
    new_dict = {}
    new_dict['id'] = id_
    new_dict['air_temperature'] = air_t
    new_dict['air_humidity'] = air_h
    new_dict['UV_index'] = uv_ind
    new_dict['soil_moisture'] = soil_m
    new_dict['plant_id__id'] = p_id
    new_dict['tiemstamp'] = timestamp
    
    return new_dict

utc_time = datetime.utcnow()
test_dict = rtn_data_dict(18, 25.0, 33.3, 12.9, 22.2, 13, utc_time)
print(test_dict)

# insert dictionary(document) into collection:

# data_collection.insert_one(test_dict)
