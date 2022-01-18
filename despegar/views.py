from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

# Create your views here.


class VehiclesViewSet(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    #def create(self, request, *args, **kwargs):
    #
    #    serializer = self.get_serializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    self.perform_create(serializer)
    #    headers = self.get_success_headers(serializer.data)
    #    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all();
    serializer_class = HotelSerializer