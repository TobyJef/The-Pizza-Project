from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from django.contrib import messages
from django.views.generic.edit import FormView, UpdateView, DeleteView

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

# User Booking View
def user_bookings(request):
    mybookings = Booking.objects.all().values()
    template = loader.get_template('user_bookings.html')
    context = { 'mybookings' : mybookings}

    return HttpResponse (template.render(context, request))
        
# /user booking view


