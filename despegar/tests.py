from django.test import TestCase
from django.test.client import Client
from despegar.models import *
from django.contrib.auth.models import User
import json

# Create your tests here.

class DespegarTestCase(TestCase):

    def setUp(self) -> None:
        self.browser = Client()
        self.client = User.objects.create(username="tomastest",
                                          email='tomastest@gmail.com',
                                          password='tomastest123',
                                          first_name='tomas',
                                          last_name='alvarez',
                                          is_active=True,
                                          is_staff=True )
        self.client.set_password("tomastest123")
        self.client.save()

        self.Country1 = Country.objects.create(name = 'Argentina')

        self.Country2 = Country.objects.create(name = 'Colombia')

        self.Province1 = Province.objects.create(name = 'Cordoba', country = self.Country1)
        
        self.Province2 = Province.objects.create(name = 'Bolivar', country = self.Country2)

        self.Airport1 = Airport.objects.create(name = 'Aeropuerto de Cordoba', province = self.Province1)

        self.Airport2 = Airport.objects.create(name = 'Aeropuerto de Colombia', province = self.Province2)

        self.Vehicle1 = Vehicle.objects.create(patent =  345678, brand = 'Mercedes', priceperday = 3700)
        
        self.Hotel1 = Hotel.objects.create( name = 'Hard Rock', hotel_type = 'Normal', stars = 5, address = 'Las Vegas 47')
        
        self.Flight1 = Flight.objects.create(code_number = 1, flight_type = 'Normal', airport_from = self.Airport1, airport_to = self.Airport2, hours = 15, date= '2022-02-12', turn = True, price = 3000)

        self.Package1 = Package.objects.create(hotel = self.Hotel1, vehicle = self.Vehicle1, flight = self.Flight1, price = 5000, amount = 5)

        self.Purchase1 = Purchase.objects.create(status = 0, user = self.client, package = self.Package1)


        response = self.browser.post('/login/', {'email': 'tomastest@gmail.com','username':'tomastest', 'password': 'tomastest123'})
        responde_js = json.loads(response.content)
        self.browser.defaults['HTTP_AUTHORIZATION'] ='Bearer {}'.format(responde_js.get('access'))



    def test_currentAmount_package_purchase(self):
        self.Purchase1.status = 1
        self.Purchase1.save()
        self.Package1.refresh_from_db()
        self.assertEqual(self.Package1.currentAmount,4)

    def test_currentAmount_package_canceled(self):
        self.Purchase1.status = 2
        self.Purchase1.save()
        self.Package1.refresh_from_db()
        self.assertEqual(self.Package1.currentAmount,5)



        
    