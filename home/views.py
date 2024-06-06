from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic

from .models import Booking, Contact
from .forms import BookingForm, ContactForm

# Booking Form

def booking_page(request):
    """
    Posts entered form data to database 
    and displays confirmation message
    """

    if request.method == "POST":
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your booking request. We will be in touch with you soon.")
            return redirect('main-page')
    else: 
        form = BookingForm()

    return render(
        request,
        "home/booking.html",
        {
            "form": form
        },
    )

# Your Bookings View

class BookingList(generic.ListView):
    """
    Displays booking details of current 
    logged in user on your-bookings page
    """

    model = Booking
    template_name = "home/your-bookings.html"
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


# All Bookings View 

class AllBookingsList(generic.ListView):
    """
    View for hosts to display all bookings
    and confirm, cancel or delete them
    """

    model = Booking
    queryset = Booking.objects.all()
    print("queryset in all bookings = ", queryset)
    template_name = "home/all-bookings.html"


# Cancel Booking View

def cancel_booking(request, booking_id):
    """
    Functionality to cancel a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)
        
    if booking.user == request.user or user.is_superuser:
        booking.booking_status = "Cancelled"
        booking.save()
        messages.add_message(request, messages.SUCCESS, 'The booking has been cancelled!')
    else:
        messages.add_message(request, messages.ERROR, 'There was an error cancelling the booking.')
    
    return HttpResponseRedirect(reverse('your-bookings'))


# Confirm Booking View

def confirm_booking(request, booking_id):
    """
    Functionality to confirm a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)
        
    if user.is_superuser:
        booking.booking_status = "Confirmed"
        booking.save()
        messages.add_message(request, messages.SUCCESS, 'The booking has been confirmed!')
    else:
        messages.add_message(request, messages.ERROR, 'There was an error confirming the booking.')

    return HttpResponseRedirect(reverse('all-bookings'))


# Contact View

def contact_page(request):
    """
    Posts guest messages to the database
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            #contact_form.instance.user = request.user
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your message. We will be in touch with you soon.")
            return redirect('main-page')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error sending your message.')
    else: 
        contact_form = ContactForm()

    return render(
        request,
        "home/contact.html",
                {
            "contact_form": contact_form
        },
    )


# Template Views

def all_bookings_page(request):
    return render(request, 'home/all-bookings.html')

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

def main_page(request):
    return render(request, 'home/index.html')

def day_trips_page(request):
    return render(request, 'home/day-trips.html')

def about_us_page(request):
    return render(request, 'home/about-us.html')

def your_bookings_page(request):
    return render(request, 'home/your-bookings.html')