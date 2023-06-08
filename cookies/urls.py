from django.urls import path
from . import views

app_name = 'cookies'

urlpatterns = [
    path('', views.home, name='home'),
    path('cookies/<int:id>/', views.cookie, name='cookie'),
]
