from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.


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


class Hotel(models.Model):
    STARS = ((0, '0 estrellas'),
             (1, '1 estrella'),
             (2, '2 estrellas'),
             (3, '3 estrellas'),
             (4, '4 estrellas'),
             (5, '5 estrellas'),
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
                    choices=STARS)
    address = models.CharField(max_length=50)
    priceperday = models.FloatField(verbose_name="Price per day",
                    default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class Vehicle(models.Model):
    patent = models.IntegerField()
    brand = models.CharField(max_length=20)
    priceperday = models.FloatField(verbose_name="Price per day",
                    default=0.00)

    def __str__(self):
        return (f"Vehicle: {self.patent} - {self.brand}")

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'


class Flight(models.Model):

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
    price = models.FloatField()

    def __str__(self):
        return (f"Flight: {self.code_number} - From: {self.airport_from.only_name()} - To: {self.airport_to.only_name()}")

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
