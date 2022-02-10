from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('despegar.urls', 'despegar')),
    path('', include('login.urls')),
]
