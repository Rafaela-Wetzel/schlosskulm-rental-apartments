from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user_name")
    booking_date = models.DateField(auto_now=True)
    status = (
        ('Requested', 'Requested'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )
    booking_status = models.CharField(choices=status, blank=True, null=True, default='Requested')
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    booking_object = (
        ('Upper Apartment', 'Upper Apartment'),
        ('Lower Apartment', 'Lower Apartment'),
        ('Whole House', 'Whole House'),
    )
    booking_item = models.CharField(choices=booking_object)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    guest_number = (
        ('1', '1'),
        ('2', '2'), 
        ('3', '3'), 
        ('4', '4'), 
        ('5', '5'), 
        ('6', '6'), 
        ('7', '7'), 
        ('8', '8'), 
        ('9', '9'), 
        ('10', '10'), 
        ('11', '11'), 
        ('12', '12'), 
        ('13', '13'), 
        ('14', '14'), 
        ('15', '15'), 
    )
    amount_guests = models.CharField(choices=guest_number)
    guest_nationality = (
        ('German', 'German'),
        ('Other', 'Other'),
    )
    nationality = models.CharField(choices=guest_nationality)
    passport_number = models.CharField(max_length=100, blank=True, null=True)
    animals = models.BooleanField(blank=True, null=True)
    message = models.TextField(max_length=1000)

    class Meta:
        ordering=['last_name','first_name']

    def __str__(self):
        return f'Booking: {self.last_name}, {self.first_name}'