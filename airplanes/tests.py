# airplanes/tests.py
from django.test import TestCase
from .models import Airplane

class AirplaneModelTest(TestCase):

    def test_create_airplane(self):
        airplane = Airplane.objects.create(id=1, passenger_capacity=200)
        self.assertEqual(airplane.id, 1)
        self.assertEqual(airplane.passenger_capacity, 200)

    def test_fuel_tank_capacity(self):
        airplane = Airplane.objects.create(id=2, passenger_capacity=150)
        self.assertEqual(airplane.fuel_tank_capacity(), 400)

    def test_fuel_consumption_per_minute(self):
        airplane = Airplane.objects.create(id=3, passenger_capacity=100)
        expected_consumption = 0.80 * 3 + 0.002 * 100
        self.assertAlmostEqual(airplane.fuel_consumption_per_minute(), expected_consumption, places=2)

    def test_fuel_consumption_per_minute_with_zero_passenger_capacity(self):
        airplane = Airplane.objects.create(id=4, passenger_capacity=0)
        expected_consumption = 0.80 * 4
        self.assertAlmostEqual(airplane.fuel_consumption_per_minute(), expected_consumption, places=2)

    def test_fuel_consumption_per_minute_with_large_passenger_capacity(self):
        airplane = Airplane.objects.create(id=5, passenger_capacity=1000)
        expected_consumption = 0.80 * 5 + 0.002 * 1000
        self.assertAlmostEqual(airplane.fuel_consumption_per_minute(), expected_consumption, places=2)