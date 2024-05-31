from django.urls import path
from . import views


urlpatterns = [
    path('booking/your-bookings/', views.BookingList.as_view(), name='your-bookings'), 
]