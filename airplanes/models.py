from django.db import models

class Airplane(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    passenger_capacity = models.PositiveIntegerField()

    def fuel_tank_capacity(self):
        return 200 * self.id

    def fuel_consumption_per_minute(self):
        base_consumption = 0.80 * self.id
        passenger_consumption = 0.002 * self.passenger_capacity
        return base_consumption + passenger_consumption
