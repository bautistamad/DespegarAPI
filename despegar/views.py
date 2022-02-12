from getpass import getuser
from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class VehiclesViewSet(viewsets.ModelViewSet, ProductPermissions):

    """
    Vehiculos
    list:
        Permite listar los vehiculos
    create:
        Permite crear un vehiculo (es necesario ser superusuario)
    read:
        Permite listar un vehiculo en especifico
    update:
        Permite modificar completamente un vehiculo (no soportado)
    partial_update:
        Permite modificar parcialmente un vehiculo (no soportado)
    delete:
        Permite eliminar un vehiculo (es necesario ser superusuario)
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [ProductPermissions]
    
    def get_queryset(self):
        """
        Si es superusuario devuelve todos los vehiculos,
        sino devuelve solo los disponibles
        """
        if self.request.user.is_superuser:
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
            return Response("Can not create vehicle, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

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
            return Response("Can not remove vehicle, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class HotelsViewSet(viewsets.ModelViewSet, ProductPermissions):
    
    """
    Hoteles
    list:
        Permite listar los hoteles
    create:
        Permite crear un hotel (es necesario ser superusuario)
    read:
        Permite listar un hotel en especifico
    update:
        Permite modificar completamente un hotel (no soportado)
    partial_update:
        Permite modificar parcialmente un hotel (no soportado)
    delete:
        Permite eliminar un hotel (es necesario ser superusuario)
    """

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los hoteles,
        sino devuelve solo los disponbles 
        """
        if self.request.user.is_superuser:
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
            return Response("Can not create hotel, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

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
            return Response("Can not remove hotel, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class FlightsViewSet(viewsets.ModelViewSet, ProductPermissions):
    
    """
    Vuelos
    list:
        Permite listar los vuelos
    create:
        Permite crear un vuelo (es necesario ser superusuario)
    read:
        Permite listar un vuelo en especifico
    update:
        Permite modificar completamente un vuelo (no soportado)
    partial_update:
        Permite modificar parcialmente un vuelo (no soportado)
    delete:
        Permite eliminar un vuelo (es necesario ser superusuario)
    """
    
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los vuelos,
        sino devuelve solo los disponbles 
        """
        
        if self.request.user.is_superuser:
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
            return Response("Can not create flight, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

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
            return Response("Can not remove flight, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class AirportViewSet(viewsets.ModelViewSet, ProductPermissions):
    """
    Aeropuertos
    list:
        Permite listar los aeropuertos
    create:
        Permite crear un aeropuerto (es necesario ser superusuario)
    read:
        Permite listar un aeropuerto en especifico
    update:
        Permite modificar completamente un aeropuerto (no soportado)
    partial_update:
        Permite modificar parcialmente un aeropuerto (no soportado)
    delete:
        Permite eliminar un aeropuerto (es necesario ser superusuario)
    """

    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los aeropuertos,
        sino devuelve solo los disponbles 
        """
        return Airport.objects.all()

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos aeropuertos
        * Agarra los parametros y crea el aeropuerto
        """
        name = request.data["name"]
        province = request.data["province"]

        try:
            created = Airport.objects.create(
                name = name,
                province = province
            )
            created.save()

            return Response("New airport created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can not create airport, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar aeropuestos
        * Utiliza el id, busca y borra el aeropuesto
        """
        try:
            airport_id = request.data["id"]
            airport = get_object_or_404(Airport, id=airport_id)
            airport.delete()
            return Response("Airport removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can not remove airport, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class ProvinceViewSet(viewsets.ModelViewSet, ProductPermissions):
    
    """
    provincias
    list:
        Permite listar los provincias
    create:
        Permite crear un provincia (es necesario ser superusuario)
    read:
        Permite listar un provincia en especifico
    update:
        Permite modificar completamente un provincia (no soportado)
    partial_update:
        Permite modificar parcialmente un provincia (no soportado)
    delete:
        Permite eliminar un provincia (es necesario ser superusuario)
    """

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si le paso un argumento de pais devuelve las provincias de dicho pais
        , sino devuelve todas las provincias
        """
        country_name = self.request.query_params.get('country') 
        if country_name:
            return Province.objects.filter(country__name=country_name)
        else:
            return Province.objects.all()


    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos paises
        * Agarra los parametros y crea el pais
        """
        name = request.data["name"]
        country = request.data["country"]

        try:
            created = Province.objects.create(
                name = name,
                country = country
            )
            created.save()

            return Response("New province created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can not create province, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar paises
        * Utiliza el id, busca y borra el pais
        """
        try:
            province_id = request.data["id"]
            province = get_object_or_404(Province, id=province_id)
            province.delete()
            return Response("Province removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can not remove province, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class CountryViewSet(viewsets.ModelViewSet, ProductPermissions):
   
    """
    Paises
    list:
        Permite listar los paises
    create:
        Permite crear un pais (es necesario ser superusuario)
    read:
        Permite listar un pais en especifico
    update:
        Permite modificar completamente un pais (no soportado)
    partial_update:
        Permite modificar parcialmente un pais (no soportado)
    delete:
        Permite eliminar un pais (es necesario ser superusuario)
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los paises,
        sino devuelve solo los disponbles 
        """
        return Country.objects.all()

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos paises
        * Agarra los parametros y crea el pais
        """
        name = request.data["name"]

        try:
            created = Country.objects.create(
                name = name,
            )
            created.save()

            return Response("New country created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can not create country, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar paises
        * Utiliza el id, busca y borra el pais
        """
        try:
            country_id = request.data["id"]
            country = get_object_or_404(Country, id=country_id)
            country.delete()
            return Response("Country removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can not remove country, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class PackageViewSet(viewsets.ModelViewSet, ProductPermissions):
    
    """
    Paquetes
    list:
        Permite listar los paquetes
    create:
        Permite crear un paquete (es necesario ser superusuario)
    read:
        Permite listar un paquete en especifico
    update:
        Permite modificar completamente un paquete (no soportado)
    partial_update:
        Permite modificar parcialmente un paquete (no soportado)
    delete:
        Permite eliminar un paquete (es necesario ser superusuario)
    """
    
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los paquetes,
        sino devuelve solo los disponIbles 
        """
        if self.request.user.is_superuser:
            return Package.objects.all()

        country_name = self.request.query_params.get('country')
        
        if country_name:
            return Package.objects.filter(flight__airport_to__province__country__name=country_name)

        return Package.objects.filter(status=0)

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos paquetes
        * Agarra los parametros y crea el paquete
        """
        hotel = request.data["hotel"]
        vehicle = request.data["vehicle"]
        flight = request.data["flight"]
        price = request.data["price"]
        amount = request.data["amount"]

        try:
            created = Package.objects.create(
                hotel = hotel,
                vehicle = vehicle,
                flight = flight,
                price = price
            )
            created.save()

            return Response("New package created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can not create package, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar paquetes
        * Utiliza el id, busca y borra el paquete
        """
        try:
            package_id = request.data["id"]
            package = get_object_or_404(Package, id=package_id)
            package.delete()
            return Response("Package removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can not remove package, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class PurchaseViewSet(viewsets.ModelViewSet, PackagePermissions):
    
    """
    Compras
    list:
        Permite listar las compras
    create:
        Permite crear una compra (es necesario ser superusuario)
    read:
        Permite listar una compra en especifico
    update:
        Permite modificar completamente una compra (no soportado)
    partial_update:
        Permite modificar parcialmente una compra (no soportado)
    delete:
        Permite eliminar una compra (es necesario ser superusuario)
    """
    
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [PackagePermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los purchase,
        sino devuelve solo los disponibles 
        """
        user = self.request.user
        purchases = Purchase.objects.filter(status=0,user=user);
        return purchases
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset :
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response("You have no current / on going purchase", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """
        El usuario solo puede crear nuevos purchases si no tiene ninguno en proceso
        * Agarra los parametros y crea el paquete
        """
        package = request.data["package"]
        package = Package.objects.filter(id=package).first()

        user = self.request.user

        lastPurchase = Purchase.objects.filter(user=user,status=0).first()
        if lastPurchase:
            return Response("A purchase is already being processed", status=status.HTTP_400_BAD_REQUEST)

        try:
            created = Purchase.objects.create(
                package = package,
                user = user
            )
            created.save()
            return Response("New purchase created", status=status.HTTP_201_CREATED)
        except:
            return Response("Can not create purchase, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        modifiedStatus = request.data['status']
        if modifiedStatus in Purchase.STATUS_NUMBER:
            lastPurchase = Purchase.objects.filter(user=user,status=0).first()
            if not lastPurchase:
                return Response("There's no purchase to modify", status=status.HTTP_400_BAD_REQUEST)
            lastPurchase.status = modifiedStatus
            lastPurchase.save()
            if modifiedStatus == 1:
                return Response("Purchase has been closed", status=status.HTTP_206_PARTIAL_CONTENT)
            else:
                return Response("Purchase has been canceled", status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            return Response("Status code doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar purchases
        * Utiliza el id, busca y borra el purchase
        """
        try:
            purchase_id = request.data["id"]
            purchase = get_object_or_404(Purchase, id=purchase_id)
            purchase.delete()
            return Response("Purchase removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can not remove purchase, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

