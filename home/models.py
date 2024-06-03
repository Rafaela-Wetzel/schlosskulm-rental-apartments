import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils import timezone, dateformat
from django.forms import forms

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user_name", default='1')
    slug = models.SlugField(max_length=200, unique=True)
    booking_date = models.DateTimeField(default=now)
    status = (
        ('Requested', 'Requested'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )
    booking_status = models.CharField(choices=status, blank=True, null=True, default='Requested')
    first_name = models.CharField(max_length=100, default="Henna")
    last_name = models.CharField(max_length=100, default="Hamma")
    birth_date = models.DateField(help_text = "Please enter data in the format '2006-10-25'", default="2006-10-25")
    email = models.EmailField(max_length=100, default="hello@gmx.de")
    phone_number = models.BigIntegerField(default="123")
    address = models.CharField(max_length=200, default="Hello street 6")
    zip_code = models.CharField(max_length=100, default="12345")
    city = models.CharField(max_length=100, default="Monster City")
    country = models.CharField(max_length=100, default="Monster Country")
    booking_object = (
        ('Upper Apartment', 'Upper Apartment'),
        ('Lower Apartment', 'Lower Apartment'),
        ('Whole House', 'Whole House'),
    )
    booking_item = models.CharField(choices=booking_object, default="Upper Apartment")
    arrival_date = models.DateField(help_text = "Please enter data in the format '2006-10-25'", default="2024-10-30")
    departure_date = models.DateField(help_text = "Please enter data in the format '2006-10-25'", default="2024-10-31")
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
    amount_guests = models.CharField(choices=guest_number, default="1")
    guest_nationality = (
        ('German', 'German'),
        ('Other', 'Other'),
    )
    nationality = models.CharField(choices=guest_nationality, default="German")
    passport_number = models.CharField(max_length=100, blank=True, null=True, default="234")
    animals = models.BooleanField(blank=True, null=True)
    message = models.TextField(max_length=1000, default="Hi!")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.last_name}, {self.first_name} (booked {self.booking_date})'

    # Date Validation

    def clean(self):
        arrival_date = self.arrival_date
        departure_date = self.departure_date
        birth_date = self.birth_date
	 
        if departure_date < arrival_date:
            raise forms.ValidationError("Your arrival date must be before your departure date!")
        elif departure_date == arrival_date:
            raise forms.ValidationError("Your arrival date cannot be the same day as your departure date!")
        elif arrival_date < datetime.date.today():
            raise forms.ValidationError("Your booking dates cannot be in the past!")
        elif departure_date < datetime.date.today():
            raise forms.ValidationError("Your booking dates cannot be in the past!")
        elif birth_date > datetime.date.today():
            raise forms.ValidationError("Your birth date cannot be in the future!")
