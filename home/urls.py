from django.urls import path
from . import views


urlpatterns = [
    path('your-bookings/', views.BookingList.as_view(), name='your-bookings'), 
    path('all-bookings/', views.AllBookingsList.as_view(), name='all-bookings'),
]