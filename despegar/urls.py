from posixpath import basename
from django.urls import path
from despegar.views import *
from rest_framework.routers import DefaultRouter

app_name = "despegar"

router = DefaultRouter()
router.register("vehicles", VehiclesViewSet, basename="vehicles")
router.register("hotels", HotelsViewSet, basename="hotels")

urlpatterns = router.urls

