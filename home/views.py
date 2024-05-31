from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic

from .models import Booking
from .forms import BookingForm

# Booking Form

def booking_page(request):
    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your booking request. We will be in touch with you soon.")
            return redirect("https://schlosskulm-762627e86384.herokuapp.com/")
    else: 
        form = BookingForm()

    return render(
        request,
        "home/booking.html",
        {
            "form": form
        },
    )

# Booking View

class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "home/your-bookings.html"

# Template Views

def directions_page(request):
    return render(request, 'home/directions.html')

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

def your_bookings_page(request):
    return render(request, 'home/your-bookings.html')