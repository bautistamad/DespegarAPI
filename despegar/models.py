from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Pais'
        verbose_name_plural='Paises'

class Province(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='Pais',null=True)

    def __str__(self):
        return self.name + " - " + self.country.name

    class Meta:
        verbose_name='Provincia'
        verbose_name_plural='Provincias'

class Airport(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province,on_delete=models.CASCADE,related_name='Provincia',null=True)

    def __str__(self):
        return self.name + " - " + self.province.name + " - " + self.province.country.name

    class Meta:
        verbose_name='Aeropuerto'
        verbose_name_plural='Aeropuertos'

class Hotel(models.Model):
    STARS = ((0,'0 estrellas'),
            (1,'1 estrella'),
            (2,'2 estrellas'),
            (3,'3 estrellas'),
            (4,'4 estrellas'),
            (5,'5 estrellas'),
    )
    name = models.CharField(max_length=50)
    stars = models.IntegerField(default=0,choices=STARS)
    address = models.CharField(max_length=50)
    price = models.FloatField()

    class Meta:
        verbose_name='Hotel'
        verbose_name_plural='Hoteles'


class Vehicle(models.Model):
    patent = models.IntegerField()
    brand = models.CharField(max_length=20)
    price = models.FloatField()

    class Meta:
        verbose_name='Vehiculo'
        verbose_name_plural='Vehiculos'

class Flight(models.Model):
    code_number = models.IntegerField()
    airport_from = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='Desde')
    airport_to = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='Hasta')
    hours = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(99)])
    date = models.DateField()
    turn = models.BooleanField(default=False)
    price = models.FloatField()

    class Meta:
        verbose_name='Vuelos'
        verbose_name_plural='Vuelos'