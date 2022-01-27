from getpass import getuser
from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class VehiclesViewSet(viewsets.ModelViewSet, ProductPermissions):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los vehiculos,
        sino devuelve solo los disponibles
        """
        user = self.request.user
        if user.is_superuser:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(status=0)

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos vehiculos
        * Agarra los parametros y crea el vehiculo
        """
        patent = request.data['patent']
        brand = request.data['brand']
        priceperday = request.data['priceperday']
        try:
            created = Vehicle.objects.create(
                patent=patent, 
                brand=brand, 
                priceperday=priceperday)
            created.save()

            return Response("New vehicle created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can't create vehicle, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar vehiculos
        * Utiliza el id, busca y borra el vehiculo
        """
        try:
            vehicle_id = request.data["id"]
            vehicle = get_object_or_404(Vehicle, id=vehicle_id)
            vehicle.delete()
            return Response("Vehicle removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can't remove vehicle, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class HotelsViewSet(viewsets.ModelViewSet, ProductPermissions):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los hoteles,
        sino devuelve solo los disponbles 
        """
        user = self.request.user
        if user.is_superuser:
            return Hotel.objects.all()
        return Hotel.objects.filter(status=0)

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos hoteles
        * Agarra los parametros y crea el hotel
        """
        name = request.data['name']
        hotel_type = request.data['hotel_type']
        stars = request.data['stars']
        address = request.data['address']
        priceperday = request.data['priceperday']

        try:
            created = Hotel.objects.create(
                name = name,
                hotel_type = hotel_type,
                stars = stars,
                address = address,
                priceperday = priceperday
            )
            created.save()

            return Response("New hotel created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can't create hotel, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar hoteles
        * Utiliza el id, busca y borra el hotel
        """
        try:
            hotel_id = request.data["id"]
            hotel = get_object_or_404(Hotel, id=hotel_id)
            hotel.delete()
            return Response("Hotel removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can't remove hotel, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class FlightsViewSet(viewsets.ModelViewSet, ProductPermissions):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los vuelos,
        sino devuelve solo los disponbles 
        """
        user = self.request.user
        if user.is_superuser:
            return Flight.objects.all()
        return Flight.objects.filter(status=0)

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos vuelos
        * Agarra los parametros y crea el vuelo
        """

        code_number = request.data["code_number"]
        flight_type = request.data["flight_type"]
        airport_from = request.data["airport_from"]
        airport_to = request.data["airport_to"]
        hours = request.data["hours"]
        date = request.data["date"]
        turn = request.data["turn"]
        price = request.data["price"]

        try:
            created = Hotel.objects.create(
                code_number = code_number,
                flight_type = flight_type,
                airport_from = airport_from,
                airport_to = airport_to,
                hours = hours,
                date = date,
                turn = turn,
                price = price
            )
            created.save()

            return Response("New flight created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can't create flight, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar vuelos
        * Utiliza el id, busca y borra el vuelo
        """
        try:
            flight_id = request.data["id"]
            flight = get_object_or_404(Flight, id=flight_id)
            flight.delete()
            return Response("Flight removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can't remove flight, contact an administrator", status=status.HTTP_400_BAD_REQUEST)
