from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user_name")
    booking_date = models.DateField(auto_now=True)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    animals = models.BooleanField()
    amount_guests = models.IntegerField()
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100, blank=True, null=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    message = models.TextField(max_length=1000)

    class Meta:
        ordering=['last_name','first_name']

    def __str__(self):
        return f'Booking: {self.last_name}, {self.first_name}'