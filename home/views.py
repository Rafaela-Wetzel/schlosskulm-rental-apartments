from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic

from .models import Booking
from .forms import BookingForm

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


# Edit Bookings View

"""
def edit_booking(request, slug, booking_id):

    View for hosts to confirm or cancel booking

    if request.method == "POST":

        queryset = Booking.objects.filter()
        #post = get_object_or_404(queryset, slug=slug)
        booking = get_object_or_404(Booking, pk=booking_id)
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid() and user.is_authenticated:
            booking = booking_form.save(commit=False)
            booking.booking_status = booking_status
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'The booking has been updated!')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error updating the booking!')

    return HttpResponseRedirect(reverse('booking'), args=[slug])
"""

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