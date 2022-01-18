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