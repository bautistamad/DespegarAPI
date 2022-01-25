from getpass import getuser
from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from login.models import User
import jwt

# Create your views here.


class VehiclesViewSet(viewsets.ModelViewSet, DefaultPermissions):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permissions_classes = [DefaultPermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(status=1)

    def create(self, request, *args, **kwargs):
        user = get_user(request)
        if user.is_authenticated and user.is_superuser:

            patent = request.data['patent']
            brand = request.data['brand']
            priceperday = request.data['priceperday']

            created = Vehicle.objects.create(
                patent=patent, brand=brand, priceperday=priceperday)
            created.save()
            return Response("New vehicle created", status=status.HTTP_201_CREATED)
        return Response("Cant create a new vehicle", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        user = get_user(request)
        if user.is_authenticated and user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
        #Vehicle.objects.delete(id = request.data['id'])
            return Response("Vehicle removed", status=status.HTTP_204_NO_CONTENT)
        return Response("You dont have permission to delete a car", status=status.HTTP_400_BAD_REQUEST)


class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


def get_user(request):
    token = request.COOKIES.get('jwt')
    print(token)
    if not token:
        raise (AuthenticationFailed('Unauthenticated!'))
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    return (user)
