from django.forms import forms, ModelForm
from .models import Booking, Contact
from django.db import models

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'phone_number', 'address', 'zip_code', 'city', 'country', 'booking_item', 'arrival_date', 'departure_date', 'amount_guests', 'nationality', 'passport_number', 'animals', 'message']
        exclude = ['booking_date', 'booking_status']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'inquiry']
        labels = {
            "name":  "Your Name",
            "mail": "E-Mail",
            "inquiry": "Message",
        }