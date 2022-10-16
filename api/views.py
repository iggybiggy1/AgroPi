from typing import NoReturn
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework import permissions
from api.serializers import UserSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from api.models import Plant, DataPoint
from api.serializers import PlantSerializer, DataPointSerializer
from api.permissions import IsOwnerOrAdminOrReadOnly


@api_view(['POST'])
@require_http_methods(['POST'])
def register_request(request):
    """
    Register a user. Return the generated Session Token.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            User.objects.get(email=data['email'])
            return JsonResponse({'message': 'User already registered.'}, status=400)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=data['username'], email=data['email'], password=data['password'])
            token = Token.objects.create(user=user)
            return JsonResponse({'message': 'User registered sucessfully.', 'token': str(token.key)}, status=201)


@api_view(['POST'])
@require_http_methods(['POST'])
def login_request(request):
    """
    Login a user. Return a token.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            username=data['username'], password=data['password'])
        if user is not None:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return JsonResponse({'message': 'User loged in sucessfully.', 'token': str(token.key)}, status=200)
        return JsonResponse({'message': 'User not found! Please check your credentials and try agaon'}, status=404)


class PlantView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrAdminOrReadOnly]

    def get_object(self, id):
        try:
            return Plant.objects.get(pk=id)
        except Plant.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        plant = self.get_object(id)
        serializer = PlantSerializer(plant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        plant = self.get_object(id)
        serializer = PlantSerializer(plant, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        plant = self.get_object(id)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlantListView(APIView):
    """
    All plants for a specific user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrAdminOrReadOnly]

    def get(self, request, user_id, format=None):
        plants = Plant.objects.filter(user_id=user_id)
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id, format=None):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataPointView(APIView):
    """
    Access point to create a data point.
    """

    def post(self, request, format=None):
        serializer = DataPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            plant = Plant.objects.get(pk=request.data['plant'])
            error_string = self.get_error_string(
                data=request.data, plant=plant)
            if error_string.__len__() > 0:
                send_mail(
                    subject='AgroPi: Plant not in best conditions :('.format(), message=error_string, from_email=settings.EMAIL_HOST_USER, recipient_list=[plant.user.email], fail_silently=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_error_string(self, data, plant):
        result = ''
        if data['air_temperature'] > plant.best_temperature + plant.temperature_margin or data['air_temperature'] < plant.best_temperature - plant.temperature_margin:
            result += "Air temperature out of margin!\n"
        if data['air_humidity'] > plant.best_air_humidity + plant.air_humidity_margin or data['air_humidity'] < plant.best_air_humidity - plant.air_humidity_margin:
            result += "Air humidity out of margin!\n"
        if data['soil_moisture'] > plant.best_soil_moisture + plant.soil_moisture_margin or data['soil_moisture'] < plant.best_soil_moisture - plant.soil_moisture_margin:
            result += "Soil moisture out of margin!\n"
        if data['UV_index'] > plant.best_light + plant.light_margin or data['UV_index'] < plant.best_light - plant.light_margin:
            result += "Light level out of margin!\n"
        if result.__len__() > 0:
            result = "Plant {0} is not in it's best conditions: \n".format(
                plant.name) + result

        return result


class DataPointListView(APIView):
    """
    Get all data points for a specific plant.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrAdminOrReadOnly]

    def get(self, request, plant_id, format=None):
        data_points = DataPoint.objects.filter(plant_id=plant_id)
        serializer = DataPointSerializer(data_points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterPi(APIView):
    def get(self, request, format=None):
        plant = Plant.objects.create(name='New Plant')
        return Response({'plant_id': plant.id}, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        plant = Plant.objects.get(id=request.data['plant_id'])
        if request.data['username'] is not None:
            user = authenticate(
                username=request.data['username'], password=request.data['password'])
        else:
            user = authenticate(
                email=request.data['email'], password=request.data['password'])
        if user is not None:
            plant.user = user
            plant.save()
            serializer = PlantSerializer(plant)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'User not found! Make sure your credentials are correct and that you are registered.'}, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrAdminOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrAdminOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
