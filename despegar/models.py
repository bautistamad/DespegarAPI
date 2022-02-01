from telnetlib import STATUS
from django.db import models
from login import models as LoginModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.core.validators import MinValueValidator,MaxValueValidator


class Product(models.Model):
    STATUS = ((0, 'Available'),
             (1, 'Not Available'),
             (2, 'Blocked'),
             )
    status = models.IntegerField(default=0,
                    choices=STATUS,
                    validators=[MinValueValidator(0), MaxValueValidator(2)])

    @property
    def product_status(self):
        return self.STATUS[self.status][1]

    class Meta:
        abstract = True

class Country(models.Model):
    name = models.CharField(max_length=50,
            null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Province(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,
                on_delete=models.CASCADE,
                related_name='Country',
                null=True)

    def __str__(self):
        return self.name + " - " + self.country.name

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'

class Airport(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province,
                on_delete=models.CASCADE,
                related_name='Province',
                null=True)

    def __str__(self):
        return self.name + " - " + self.province.name + " - " + self.province.country.name

    def only_name(self):
        return self.name

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'

class Hotel(Product):
    STARS = ((0, 'No stars'),
             (1, '1 star'),
             (2, '2 stars'),
             (3, '3 stars'),
             (4, '4 stars'),
             (5, '5 stars'),
             )

    TYPE_NORMAL = "Normal"
    TYPE_SALE = "Sale"
    TYPE_CHOICES = {
        (TYPE_NORMAL, 'Normal'),
        (TYPE_SALE, 'Sale'),
    }

    name = models.CharField(max_length=50)
    hotel_type = models.CharField(max_length=10,
                    choices=TYPE_CHOICES,
                    default='Normal',
                    )
    stars = models.IntegerField(default=0,
                    choices=STARS,
                    validators=[MinValueValidator(0), MaxValueValidator(5)]
                    )
    address = models.CharField(max_length=50)
    priceperday = models.FloatField(verbose_name="Price per day",
                    default=0.00)

    def __str__(self):
        return f"Hotel: {self.name}"

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

class Vehicle(Product):
    patent = models.IntegerField()
    brand = models.CharField(max_length=20)
    priceperday = models.FloatField(verbose_name="Price per day",
                    default=0.00)

    def __str__(self):
        return (f"Vehicle: {self.patent} - {self.brand}")

    @property
    def name(self):
        return (f"{self.patent} - {self.brand}")

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Flight(Product):

    TYPE_NORMAL = "Normal"
    TYPE_SALE = "Sale"
    TYPE_CHOICES = {
        (TYPE_NORMAL, 'Normal'),
        (TYPE_SALE, 'Sale'),
    }

    code_number = models.IntegerField()
    flight_type = models.CharField(max_length=10,
                    choices=TYPE_CHOICES,
                    default='Normal',
                    )
    airport_from = models.ForeignKey(Airport,
                    on_delete=models.CASCADE,
                    related_name='Desde')
    airport_to = models.ForeignKey(Airport,
                    on_delete=models.CASCADE,
                    related_name='Hasta')
    hours = models.IntegerField(default=0,
                    validators=[MinValueValidator(0), MaxValueValidator(99)])
    date = models.DateField()
    turn = models.BooleanField(default=False)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return (f"Flight N: {self.code_number} - From: {self.airport_from.only_name()} - To: {self.airport_to.only_name()}")

    @property
    def name(self):
        return (f"Flight N: {self.code_number} - From: {self.airport_from.only_name()} - To: {self.airport_to.only_name()}")

    def only_name(self):
        return (f"Flight {self.code_number} - From: {self.airport_from.only_name()} - To: {self.airport_to.only_name()}")
    

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

class Package(Product):
    hotel = models.ForeignKey(Hotel,
                    on_delete=models.CASCADE,
                    related_name="hotel"
    )
    vehicle = models.ForeignKey(Vehicle,
                    on_delete=models.CASCADE,
                    related_name="vehicle"
    )
    flight = models.ForeignKey(Flight,
                    on_delete=models.CASCADE,
                    related_name="flight"
    )
    price = models.FloatField(default=0.00)
    amount = models.IntegerField(default = 0,validators=[MinValueValidator(0), MaxValueValidator(99)])
    

    def __str__(self):
        return (f"Package N {self.id}: {self.hotel} | {self.vehicle} | {self.flight.only_name()}")

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

class Purchase(models.Model):
    STATUS_NUMBER = [0,1,2]
    STATUS = (
             (0, 'In process'),
             (1, 'Purchased'),
             (2, 'Canceled'),
             )
    status = models.IntegerField(default=0,
                    choices=STATUS,
                    validators=[MinValueValidator(0), MaxValueValidator(2)])
    user  = models.ForeignKey(LoginModel.User,
                                 on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    
    def __str__(self):
        return (f"{self.user.email}'s purchase ( {self.STATUS[self.status][1]} )")

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'