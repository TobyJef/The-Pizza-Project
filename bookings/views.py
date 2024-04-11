from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking


# Home Page View
def index(request):
    return render (request,
        'bookings/index.html')

# /home page view

# Menu Page View

def menu(request):
    return render (
        request, 'bookings/menu.html')
            
# /menu page view

# Enquiries Page View

def enquiries(request):
    return render (
        request,'bookings/enquiries.html'
        )
# /enquiries page view