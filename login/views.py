from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    """
    ### Request utilizado para registrar un usuario normal
    post:
        Permite crear un usuario normal y autenticado
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    """
    ### Devuelve un Token con las credenciales del usuario
    post:
        Permite ingresar las credenciales de usuario y conseguir el token
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
