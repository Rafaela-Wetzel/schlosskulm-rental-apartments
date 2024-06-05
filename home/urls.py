from django.urls import path
from . import views


urlpatterns = [
    path('your-bookings/', views.BookingList.as_view(), name='your-bookings'), 
    path('all-bookings/', views.AllBookingsList.as_view(), name='all-bookings'),
    #path('cancel_booking/<int:booking_id>', views.cancel_booking, name='cancel_booking'),
]