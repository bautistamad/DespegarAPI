from dataclasses import field
from pickletools import read_long1
from django.db.models import fields
from despegar.models import *
from rest_framework import serializers

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["id","product_status","patent","brand","priceperday"]

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        fields = ["name","product_status","hotel_type","stars","address","priceperday"]

class FlightSerializer(serializers.ModelSerializer):
    flight_from_name = serializers.ReadOnlyField(source='airport_from.__str__')
    flight_to_name = serializers.ReadOnlyField(source='airport_to.__str__')
    class Meta:
        model = Flight
        fields = ["code_number","product_status","flight_type","flight_from_name","flight_to_name","hours","date","turn","price"]

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

    amount = serializers.SerializerMethodField()
    hotel_name = serializers.ReadOnlyField(source='hotel.name')
    flight_name = serializers.ReadOnlyField(source='flight.name')
    vehicle_name = serializers.ReadOnlyField(source='vehicle.name')

    class Meta:
        model = Package
        fields = ["id","product_status","hotel_name","flight_name","vehicle_name","price","amount"]

    def get_amount(self,instance):
        return instance.currentAmount

class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = '__all__'
