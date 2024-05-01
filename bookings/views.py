from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


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

# Booking Form View

def get_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/Thank You for choosing The Pizza Project/")

    else:
        form = BookingForm()

    return render(request, "enquiries.html", {"form":form})

# /booking form view
