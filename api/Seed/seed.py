from typing import Any
from api.models import Plant, DataPoint
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import os

user = Any
try:
    user = User.objects.get(username="Test")
except User.DoesNotExist:
    user = User.objects.create_user(
        username="Test", email="test@gmail.com", password=os.environ.get('SEED_USER_PASSWORD', 'test123'))

plant1 = Any
try:
    plant1 = Plant.objects.get(species="Abuta", name="Abuta")
except Plant.DoesNotExist:
    plant1 = Plant.objects.create(species="Abuta", name="Abuta", user=user, best_temperature=20.0, temperature_margin=5.0,
                                  best_air_humidity=80.0, air_humidity_margin=5.0, best_soil_moisture=50.0, soil_moisture_margin=10.0, best_light=7.0, light_margin=0.5)
plant2 = Any
try:
    plant2 = Plant.objects.get(species="Acacia", name="Acacia")
except Plant.DoesNotExist:
    plant2 = Plant.objects.create(species="Acacia", name="Acacia", user=user, best_temperature=17.0, temperature_margin=2.0,
                                  best_air_humidity=75.0, air_humidity_margin=2.5, best_soil_moisture=35.0, soil_moisture_margin=7.5, best_light=6.0, light_margin=2.5)

datapoints = DataPoint.objects.all()
if(datapoints.__len__() < 10):
    time = datetime.now()
    datapoint1 = DataPoint.objects.create(air_temperature=21.6, air_humidity=78.4,
                                          UV_index=7.3, soil_moisture=52.3, plant=plant1, timestamp=time)
    datapoint2 = DataPoint.objects.create(air_temperature=21.2, air_humidity=78.1,
                                          UV_index=7.0, soil_moisture=48.2, plant=plant1, timestamp=(time + timedelta(hours=1)))
    datapoint3 = DataPoint.objects.create(air_temperature=19.8, air_humidity=78.2,
                                          UV_index=7.6, soil_moisture=46.8, plant=plant1, timestamp=(time + timedelta(hours=2)))
    datapoint4 = DataPoint.objects.create(air_temperature=22.1, air_humidity=79.9,
                                          UV_index=7.5, soil_moisture=58.2, plant=plant1, timestamp=(time + timedelta(hours=3)))
    datapoint5 = DataPoint.objects.create(air_temperature=21.5, air_humidity=79.2,
                                          UV_index=7.4, soil_moisture=54.7, plant=plant1, timestamp=(time + timedelta(hours=4)))
    datapoint6 = DataPoint.objects.create(air_temperature=17.6, air_humidity=75.02,
                                          UV_index=6.1, soil_moisture=36.2, plant=plant2, timestamp=time)
    datapoint7 = DataPoint.objects.create(air_temperature=17.3, air_humidity=76.14,
                                          UV_index=6.15, soil_moisture=35.9, plant=plant2, timestamp=(time + timedelta(hours=1)))
    datapoint8 = DataPoint.objects.create(air_temperature=17.4, air_humidity=76.09,
                                          UV_index=6.09, soil_moisture=35.2, plant=plant2, timestamp=(time + timedelta(hours=2)))
    datapoint9 = DataPoint.objects.create(air_temperature=18.5, air_humidity=74.5,
                                          UV_index=6.3, soil_moisture=34.9, plant=plant2, timestamp=(time + timedelta(hours=3)))
    datapoint10 = DataPoint.objects.create(air_temperature=19.9, air_humidity=72.23,
                                           UV_index=7.2, soil_moisture=32.2, plant=plant2, timestamp=(time + timedelta(hours=4)))
