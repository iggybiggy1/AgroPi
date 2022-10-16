from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Plant, DataPoint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email',
                  'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'species', 'name', 'user', 'best_temperature', 'temperature_margin', 'best_air_humidity',
                  'air_humidity_margin', 'best_soil_moisture', 'soil_moisture_margin', 'best_light', 'light_margin']


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ['id', 'air_temperature', 'air_humidity',
                  'UV_index', 'soil_moisture', 'plant', 'timestamp']
