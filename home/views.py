from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Booking
from .forms import BookingForm

# Booking Form

def booking_page(request):
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for booking with us. We will be in touch with you soon.")
            return redirect("home/index.html")
        else:
            messages.add_message(request, messages.ERROR, "Please fill out all form fields.")
    else: 
        form = BookingForm()

    return render(
        request,
        "home/booking.html",
        {
            "form": form
        },
    )


# Template views

def directions_page(request):
    return render(request, 'home/directions.html')

#def booking_page(request):
#    return render(request, 'home/booking.html')

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
