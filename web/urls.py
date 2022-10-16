from web import views
from django.urls import path

app_name = 'web'
urlpatterns = [
    path('', views.LoginView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('admin/', views.admin, name='admin'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<str:id>', views.dashboard, name='dashboard'),
    path('delete_plant/<pk>', views.delete_plant, name='delete_plant'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('plant/', views.PlantView.as_view(), name='plant_view'),
    path('plant/<str:id>', views.PlantView.as_view(), name='plant_view'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.RegisterView.as_view(), name='register_view'),
    path('delete_user/<pk>', views.delete_user, name='delete_user'),
    path('toggle_staff/<pk>', views.toggle_staff, name='toggle_staff')
]
