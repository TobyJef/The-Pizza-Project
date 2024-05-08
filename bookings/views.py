from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import FormView, UpdateView, DeleteView
from bookings.user_bookings import bookings_views

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
def display_bookings(request):
    bookings = bookings.objects.all()
    return render (
        request, 'bookings/user_bookings.html', {'bookings': bookings}
    )
# /user booking view'


class BookingAmend(UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = 'amend_booking.html'
    fields = ['booking_date', 'start_time', 'end_time', 'address', 'dietary_requirements', 'booking_size']
    success_url ='/', 'bookings/user_booking.html'

    def get_queryset(self):
        return self.request.user.booking_set.all()


class BookingDelete(UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url ='/', 'bookings/user_booking.html'

    def get_queryset(self):
        return self.request.user.booking_set.all()