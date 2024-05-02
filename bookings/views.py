from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from django.contrib import messages


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

def booking(request):
    # 
    day = validWeekday(94)


    # 
    validateWeekdays = isWeekdayValid(weekdays)


    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        if booking_date or booking_time == None:
            messages.success(request, "Please select a Date")
            return redirect('bookings')

        
        request.session['booking_date'] = booking_date
        request.session['booking_time'] = booking_time

        return redirect('bookingsSubmit')


    return render(request, 'bo')