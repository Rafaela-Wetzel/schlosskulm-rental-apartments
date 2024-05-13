"""
URL configuration for schlosskulm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.start_page),
    path('admin/', admin.site.urls),
    path('buchung/', views.buchung_page),
    path('haus/', views.haus_page),
    path('haus/anfahrt/', views.anfahrt_page),
    path('haus/ferienwohnung-oben/', views.ferienwohnung_oben_page),
    path('haus/ferienwohnung-unten/', views.ferienwohnung_unten_page ),
    path('haus/hausregeln/', views.hausregeln_page),
    path('kontakt/', views.kontakt_page),
    path('preise/', views.preise_page),
    path('projektarchiv/', views.projektarchiv_page),
    path('rechtliches/agb/', views.agb_page),
    path('rechtliches/datenschutz/', views.datenschutz_page),
    path('rechtliches/impressum/', views.impressum_page),
    path('schlosskulm/gallerie/', views.gallerie_page),
    path('schlosskulm/initiativen/', views.initiativen_page),
    path('schlosskulm/tagesausflug/', views.tagesausflug_page),
    path('ueber-uns/', views.ueber_uns_page),
]
