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

# urlpatterns = [
#     path('vehicles/', VehiclesViewSet.as_view({'get': 'list'}), name="vehicles"),
#     path('hotels/', HotelsViewSet.as_view({'get': 'list'}), name="hotels"),
#     path('flights/', FlightsViewSet.as_view({'get': 'list'}), name="flights"),
#     path('airports/', AirportViewSet.as_view({'get': 'list'}), name="airports"),
#     path('provinces/', ProvinceViewSet.as_view({'get': 'list'}), name="provinces"),
#     path('countries/', CountryViewSet.as_view({'get': 'list'}), name="countries"),
#     path('packages/', PackageViewSet.as_view({'get': 'list'}), name="packages"),
#     path('purchases/', PurchaseViewSet.as_view({'get': 'list'}), name="purchases")
# ]
