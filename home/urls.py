from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingList.as_view(), name='your-bookings'), 
    #path('bookings/edit_booking/<int:booking_id>',
    #     views.booking_edit, name='booking_edit'),
]