from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic import CreateView
from .forms import BookingForm



def index(request):
    """"Home Page View"""
    return render (request,
        'bookings/index.html')
# /home page view



def menu(request):
    """"Menu Page View"""
    return render (
        request, 'bookings/menu.html')          
# /menu page view



""""Enquiries Page View"""
def enquiries(request):
    return render (
        request,'bookings/enquiries.html'
        )
# /enquiries page view


""""My Bookings Page View"""
def user_bookings(request):
    model = Booking
    bookings = Booking.objects.all()
    success_url = "user_bookings.html"

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super(user_bookings, self).form_valid(form)

    return render (
        request, 'bookings/user_bookings.html', {'bookings': bookings}
    )
# /user booking view'


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """"Edit Booking"""
    form_class = Booking
    model = Booking
    template_name = 'edit_booking.html'
    fields = ['booking_date', 'start_time', 'end_time', 'address', 'dietary_requirements', 'booking_size']
    
    def form_valid(self,form):
        self.success_url ='/', 'bookings/user_booking.html'

    def get_queryset(self):
        return self.request.user.booking_set.all()


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """"Delete Booking"""
    model = Booking
    template_name = 'delete_booking.html'
    success_url ='/', 'bookings/user_booking.html'

    def get_queryset(self):
        return self.request.user.booking_set.all()