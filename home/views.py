from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from .models import Booking

# Template views

def directions_page(request):
    return render(request, 'home/directions.html')

def booking_page(request):
    return render(request, 'home/booking.html')

def upper_apartment_page(request):
    return render(request, 'home/upper-apartment.html')

def lower_apartment_page(request):
    return render(request, 'home/lower-apartment.html')

def gallery_page(request):
    return render(request, 'home/gallery.html')

def house_page(request):
    return render(request, 'home/house.html')

def house_rules_page(request):
    return render(request, 'home/house-rules.html')

def contact_page(request):
    return render(request, 'home/contact.html')

def main_page(request):
    return render(request, 'home/index.html')

def day_trips_page(request):
    return render(request, 'home/day-trips.html')

def about_us_page(request):
    return render(request, 'home/about-us.html')

# Booking Form

def book_apartment(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for booking with us. We will be in touch with you soon.")
            return redirect(main_page)
        else:
            messages.add_message(request, messages.ERROR, "Please fill out all form fields.")

    form = BookingForm()
    return render(
        request,
        "home/index.html",
        )