-------------------------------------------------------------

To Create: 

Set the request type to POST.
Set the URL to "http://127.0.0.1:8000/api/calculate_fuel_consumption/"
Set the request body to JSON with the airplane data 
{
  "airplanes": [
    {"id": 1, "passenger_capacity": 100},
    {"id": 2, "passenger_capacity": 10},
    {"id": 3, "passenger_capacity": 10},
    {"id": 4, "passenger_capacity": 70},
    {"id": 5, "passenger_capacity": 100},
    {"id": 6, "passenger_capacity": 30},
    {"id": 7, "passenger_capacity": 10},
    {"id": 8, "passenger_capacity": 20},
    {"id": 9, "passenger_capacity": 100},
    {"id": 10, "passenger_capacity": 50}
  ]
}

-------------------------------------------------------------

Expected Response: 
{
    "total_fuel_consumption": 44.00000000000001,
    "max_minutes_to_fly": 238.09523809523807
}
-------------------------------------------------------------
