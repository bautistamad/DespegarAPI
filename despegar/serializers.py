from dataclasses import field
from pickletools import read_long1
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

class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Province
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Airport
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):

    hotel_name = serializers.ReadOnlyField(source='hotel.name')
    flight_name = serializers.ReadOnlyField(source='flight.name')
    vehicle_name = serializers.ReadOnlyField(source='vehicle.name')

    class Meta:
        model = Package
        fields = ["id","product_status","hotel_name","flight_name","vehicle_name","price"]


class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = '__all__'
