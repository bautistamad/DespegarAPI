from dataclasses import field
from django.db.models import fields
from despegar.models import *
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hotel
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Airport
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = '__all__'