from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from api.models import Plant, DataPoint
from web.forms import LoginForm, RegisterForm, PlantForm
from django.views.generic import View

# Create your views here.
dashboard_path = 'web:dashboard'


@require_http_methods(['GET'])
def about(request):
    return render(request=request, template_name='web/about.html')


@require_http_methods(['GET'])
def contact(request):
    return render(request=request, template_name='web/contact.html')


@login_required(login_url='/web/')
@require_http_methods(['GET'])
def dashboard(request, id=None):
    datapoints = []
    plants = []
    plant = None
    if Plant.objects.filter(user=request.user).__len__() > 0:
        plants = request.user.plant_set.all()
        try:
            if id is not None:
                plant = Plant.objects.get(pk=id)
            else:
                plant = request.user.plant_set.all().first()
            if DataPoint.objects.filter(plant=plant).__len__() > 0:
                datapoints = plant.datapoint_set.all()
        except Plant.DoesNotExist:
            return redirect(dashboard_path)
    context = {
        'datapoints': datapoints,
        'plants': plants,
        'plant': plant,
        'adminrights': request.user.is_staff
    }

    return render(request=request, template_name='web/dashboard.html', context=context)


def staff_required(login_url='/web/'):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)


@login_required(login_url='/web/')
@staff_required(login_url='/web/')
@require_http_methods(['GET'])
def admin(request):
    users = User.objects.all()
    context = {
        'title': 'Admin',
        'username': request.user.username,
        'users': users
    }
    return render(request=request, template_name='web/adminuser.html', context=context)


@login_required(login_url='/web/')
def profile(request):
    plants = []
    plant_id = None
    form = PlantForm(data={'user': request.user})
    if Plant.objects.filter(user=request.user).__len__() > 0:
        plants = request.user.plant_set.all()
        plant_id = request.user.plant_set.all().first().id
    context = {
        'title': 'Profile | {0}'.format(request.user.username),
        'plants': plants,
        'username': request.user.username,
        'plantId': plant_id,
        'form': form,
        'adminrights': request.user.is_staff
    }
    return render(request=request, template_name='web/profile.html', context=context)


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(dashboard_path)
        form = RegisterForm()
        return render(request=request, template_name='web/register.html', context={'form': form})

    def post(self, request, backend='django.contrib.auth.backends.ModelBackend'):
        if request.user.is_authenticated:
            return redirect(dashboard_path)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'), email=form.cleaned_data.get('email'))
            login(request, user, backend=backend)
            return redirect(dashboard_path)
        return render(request=request, template_name='web/register.html', context={'form': form})


@require_http_methods(['GET'])
def logout_view(request):
    logout(request)
    return redirect("web:login_view")


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(dashboard_path)
        form = LoginForm()
        return render(request=request, template_name='web/login.html', context={'form': form})

    def post(self, request, backend='django.contrib.auth.backends.ModelBackend'):
        if request.user.is_authenticated:
            return redirect(dashboard_path)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user, backend=backend)
                plant_id = user.plant_set.all().first().id
                return redirect(dashboard_path, id=plant_id)
            else:
                return redirect("web:login_view")
        return render(request=request, template_name='web/login.html', context={'form': form})


class PlantView(LoginRequiredMixin, View):
    login_url = '/web/'

    def post(self, request, id=None):
        form = PlantForm(data={'user': request.user})
        if id is None:
            form = PlantForm(data=request.POST)
        else:
            try:
                plant = Plant.objects.get(pk=id, user=request.user)
            except Plant.DoesNotExist:
                return redirect('web:profile')
            form = PlantForm(data=request.POST, instance=plant)
        if form.is_valid():
            plant = form.save(commit=False)
            if id is None:
                Plant.objects.create_plant(name=plant.name, species=plant.species, user=plant.user, best_temperature=plant.best_temperature, temperature_margin=plant.temperature_margin, best_air_humidity=plant.best_air_humidity,
                                           air_humidity_margin=plant.air_humidity_margin, best_soil_moisture=plant.best_soil_moisture, soil_moisture_margin=plant.soil_moisture_margin, best_light=plant.best_light, light_margin=plant.light_margin)
            else:
                form.save()
            return redirect('web:profile')
        return render(request=request, template_name='web/plant.html', context={'form': form, 'plant': plant})

    def get(self, request, id=None):
        form = PlantForm(data={'user': request.user})
        if id is not None:
            plant = Plant.objects.get(pk=id)
            form = PlantForm(instance=plant)
        return render(request=request, template_name='web/plant.html', context={'form': form, 'plant': plant})


@login_required(login_url='/web/')
@require_http_methods(['GET'])
def delete_plant(request, pk):
    if request.method == "GET":
        Plant.objects.get(pk=pk).delete()
        return redirect("web:profile")


@login_required(login_url='/web/')
@staff_required(login_url='/web/')
@require_http_methods(['GET'])
def delete_user(request, pk):
    if request.method == "GET":
        User.objects.get(pk=pk).delete()
        return redirect("web:admin")


@login_required(login_url='/web/')
@staff_required(login_url='/web/')
@require_http_methods(['GET'])
def toggle_staff(request, pk):
    if request.method == "GET":
        user = User.objects.get(pk=pk)
        user.is_staff = not user.is_staff
        user.save()
        return redirect('web:admin')
