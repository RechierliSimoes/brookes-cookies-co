from django.urls import path
from cookies.views import home

urlpatterns = [
    path('', home),
]
