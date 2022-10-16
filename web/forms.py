from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.forms import Form
from django.forms.widgets import SelectDateWidget
from api.models import Plant, DataPoint


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'id': 'username', 'placeholder': 'Enter username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'id': 'password', 'placeholder': 'Enter password'})


class RegisterForm(UserCreationForm):
    classes = 'form-control'
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': self.classes, 'id': 'username', 'placeholder': 'Enter username'})
        self.fields['email'].widget.attrs.update(
            {'class': self.classes, 'id': 'email', 'placeholder': 'Enter email'})
        self.fields['password1'].widget.attrs.update(
            {'class': self.classes, 'id': 'password', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update(
            {'class': self.classes, 'id': 'confirm-password', 'placeholder': 'Confirm password'})


class PlantForm(forms.ModelForm):
    classes = 'form-control mx-sm-3'

    class Meta:
        model = Plant
        fields = ['species', 'name', 'best_temperature', 'temperature_margin', 'best_air_humidity',
                  'air_humidity_margin', 'best_soil_moisture', 'soil_moisture_margin', 'best_light', 'light_margin', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['species'].widget.attrs.update(
            {'class': self.classes, 'id': 'species', 'placeholder': 'Choose species'})
        self.fields['name'].widget.attrs.update(
            {'class': self.classes, 'id': 'name', 'placeholder': 'Enter name'})
        self.fields['best_temperature'].widget.attrs.update(
            {'class': self.classes, 'id': 'best_temperature', 'placeholder': 'Enter best temperature'})
        self.fields['temperature_margin'].widget.attrs.update(
            {'class': self.classes, 'id': 'temperature_margin', 'placeholder': 'Enter temperature margin'})
        self.fields['best_air_humidity'].widget.attrs.update(
            {'class': self.classes, 'id': 'best_air_humidity', 'placeholder': 'Enter best air humidity'})
        self.fields['air_humidity_margin'].widget.attrs.update(
            {'class': self.classes, 'id': 'air_humidity_margin', 'placeholder': 'Enter air humidity margin'})
        self.fields['best_soil_moisture'].widget.attrs.update(
            {'class': self.classes, 'id': 'best_soil_moisture', 'placeholder': 'Enter best soil moisture'})
        self.fields['soil_moisture_margin'].widget.attrs.update(
            {'class': self.classes, 'id': 'soil_moisture_margin', 'placeholder': 'Enter soil moisture margin'})
        self.fields['best_light'].widget.attrs.update(
            {'class': self.classes, 'id': 'best_light', 'placeholder': 'Enter best light'})
        self.fields['light_margin'].widget.attrs.update(
            {'class': self. classes, 'id': 'light_margin', 'placeholder': 'Enter light margin'})


class DataPointForm(forms.ModelForm):

    class Meta:
        model = DataPoint
        fields = ['air_temperature', 'air_humidity',
                  'UV_index', 'soil_moisture', 'plant', 'timestamp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['air_temperature'].widget.attrs.update(
            {'class': 'form-control', 'id': 'air_temperature', 'placeholder': 'Enter air temperature'})
        self.fields['air_humidity'].widget.attrs.update(
            {'class': 'form-control', 'id': 'air_humidity', 'placeholder': 'Enter air humidity'})
        self.fields['UV_index'].widget.attrs.update(
            {'class': 'form-control', 'id': 'UV_index', 'placeholder': 'Enter light level'})
        self.fields['soil_moisture'].widget.attrs.update(
            {'class': 'form-control', 'id': 'soil_moisture', 'placeholder': 'Enter soil moisture'})
        self.fields['plant'].widget.attrs.update(
            {'class': 'form-control', 'id': 'plant', 'placeholder': 'Enter plant'})
        self.fields['timestamp'].widget.attrs.update(
            {'class': 'form-control', 'id': 'timestamp', 'placeholder': 'Enter time'})
