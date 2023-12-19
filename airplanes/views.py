# airplanes/views.py
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import AirplaneSerializer

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def calculate_fuel_consumption(request):
    airplanes_data = request.data.get('airplanes', [])
    
    total_fuel_consumption = 0
    max_minutes_to_fly = float('inf')

    for data in airplanes_data:
        serializer = AirplaneSerializer(data=data)
        if serializer.is_valid():
            airplane = serializer.save()
            fuel_consumption = airplane.fuel_consumption_per_minute()
            total_fuel_consumption += fuel_consumption

            if airplane.passenger_capacity > 0:
                minutes_to_fly = airplane.fuel_tank_capacity() / fuel_consumption
                max_minutes_to_fly = min(max_minutes_to_fly, minutes_to_fly)

    result = {
        'total_fuel_consumption': total_fuel_consumption,
        'max_minutes_to_fly': max_minutes_to_fly,
    }

    return Response(result)
