from api import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'
urlpatterns = [
    path('register/', views.register_request),
    path('login/', views.login_request),
    # CRUD methods
    path('register_pi/', views.RegisterPi.as_view()),
    path('data_point/', views.DataPointView.as_view()),
    path('plant/<str:id>/', views.PlantView.as_view()),
    path('plants/<int:user_id>/', views.PlantListView.as_view()),
    path('data_points/<str:plant_id>/', views.DataPointListView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('login/', obtain_auth_token, name='api_token_auth'),
    # Auth methods
    # Other methods
    #path('', TemplateView.as_view(template_name='homepage.html'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
