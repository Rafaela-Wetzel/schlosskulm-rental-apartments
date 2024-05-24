from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('admin/', admin.site.urls),
    path('booking/', views.booking_page, name='booking'),
    path('house/', views.house_page, name='house'),
    path('directions/', views.directions_page, name='directions'),
    path('house/upper-apartment/', views.upper_apartment_page, name='upper-apartment'),
    path('house/lower-apartment/', views.lower_apartment_page, name='lower-apartment' ),
    path('house/house-rules/', views.house_rules_page, name='house-rules'),
    path('contact/', views.contact_page, name='contact'),
    path('schlosskulm/gallery/', views.gallery_page, name='gallery'),
    path('schlosskulm/day-trips/', views.day_trips_page, name='day-trips'),
    path('about-us/', views.about_us_page, name='about-us'),
]
