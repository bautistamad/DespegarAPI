from getpass import getuser
from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

def get_user(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise (AuthenticationFailed('Unauthenticated!'))
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    return (user)

class VehiclesViewSet(viewsets.ModelViewSet, ProductPermissions):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los vehiculos,
        sino devuelve solo los disponibles
        """
        user = get_user(self.request)
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
        user = get_user(self.request)
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
        user = get_user(self.request)
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

class AirportViewSet(viewsets.ModelViewSet, ProductPermissions):
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
            return Response("Can't create airport, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

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
            return Response("Can't remove airport, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class ProvinceViewSet(viewsets.ModelViewSet, ProductPermissions):
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
            return Response("Can't create province, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

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
            return Response("Can't remove province, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

class CountryViewSet(viewsets.ModelViewSet, ProductPermissions):
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
            return Response("Can't create country, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

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
            return Response("Can't remove country, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

# Package
# Purchase
class PackageViewSet(viewsets.ModelViewSet, ProductPermissions):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los paquetes,
        sino devuelve solo los disponbles 
        """
        user = get_user(self.request)
        if user.is_superuser:
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
            return Response("Can't create package, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar paquetes
        * Utiliza el id, busca y borra el paquete
        """
        try:
            package_id = request.data["id"]
            package = get_object_or_404(Flight, id=package_id)
            package.delete()
            return Response("Package removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can't remove package, contact an administrator", status=status.HTTP_400_BAD_REQUEST)


class PurchaseViewSet(viewsets.ModelViewSet, ProductPermissions):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [ProductPermissions]

    def get_queryset(self):
        """
        Si es superusuario devuelve todos los purchase,
        sino devuelve solo los disponibles 
        """
        user = get_user(self.request)
        # if user.is_superuser:
        #     return Purchase.objects.all()
        return Purchase.objects.filter(status=0,user=user)

    def post(self, request, *args, **kwargs):
        """
        El superusuario solo puede crear nuevos paquetes
        * Agarra los parametros y crea el paquete
        """
        hotel = request.data["hotel"]
        vehicle = request.data["vehicle"]
        flight = request.data["flight"]
        price = request.data["price"]

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
            return Response("Can't create package, contact an administrator", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        El superusuario solo puede borrar paquetes
        * Utiliza el id, busca y borra el paquete
        """
        try:
            package_id = request.data["id"]
            package = get_object_or_404(Flight, id=package_id)
            package.delete()
            return Response("Package removed", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Can't remove package, contact an administrator", status=status.HTTP_400_BAD_REQUEST)





