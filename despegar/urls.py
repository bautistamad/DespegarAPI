from posixpath import basename
from django.urls import path
from despegar.views import *
from rest_framework.routers import DefaultRouter

app_name = "despegar"

router = DefaultRouter()
router.register("vehicles", VehiclesViewSet, basename="vehicles")
router.register("hotels", HotelsViewSet, basename="hotels")
router.register("flights", FlightsViewSet, basename="flights")
router.register("airports", AirportViewSet, basename="airports")
router.register("provinces", ProvinceViewSet, basename="provinces")
router.register("countries", CountryViewSet, basename="countries")
router.register("packages", PackageViewSet, basename="packages")
router.register("purchases", PurchaseViewSet, basename="purchases")


urlpatterns = router.urls

