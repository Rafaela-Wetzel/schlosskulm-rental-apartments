from django.urls import path
from . import views


urlpatterns = [
    path('your-bookings/', views.BookingList.as_view(), name='your-bookings'), 
    path('all-bookings/', views.AllBookingsList.as_view(), name='all-bookings'),
    #path('bookings/edit_booking/<int:booking_id>',
    #     views.booking_edit, name='booking_edit'),
]