from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def agb_page(request):
    return render(request, 'home/agb.html')

def anfahrt_page(request):
    return render(request, 'home/anfahrt.html')

def buchung_page(request):
    return render(request, 'home/buchung.html')

def datenschutz_page(request):
    return render(request, 'home/datenschutz.html')

def ferienwohnung_oben_page(request):
    return render(request, 'home/ferienwohnung-oben.html')

def ferienwohnung_unten_page(request):
    return render(request, 'home/ferienwohnung-unten.html')

def gallerie_page(request):
    return render(request, 'home/gallerie.html')

def haus_page(request):
    return render(request, 'home/haus.html')

def hausregeln_page(request):
    return render(request, 'home/hausregeln.html')

def impressum_page(request):
    return render(request, 'home/impressum.html')

def initiativen_page(request):
    return render(request, 'home/initiativen.html')

def kontakt_page(request):
    return render(request, 'home/kontakt.html')

def preise_page(request):
    return render(request, 'home/preise.html')

def projektarchiv_page(request):
    return render(request, 'home/projektarchiv.html')

def start_page(request):
    return render(request, 'home/index.html')

def tagesausflug_page(request):
    return render(request, 'home/tagesausflug.html')

def ueber_uns_page(request):
    return render(request, 'home/ueber-uns.html')