from django.urls import path
from .views import calculate_fuel_consumption

urlpatterns = [
    path('calculate_fuel_consumption/', calculate_fuel_consumption, name='calculate_fuel_consumption'),
]
