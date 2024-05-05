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

def user_booking(request):
    return render (
        request, 'bookings/user_booking.html'
    )


def booking(request):
    # 
    day = validWeekday(94)


    # 
    validateWeekdays = isWeekdayValid(weekdays)


    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        if booking_date or start_time or end_time == None:
            messages.success(request, "Please select a Date or Start/End Time")
            return redirect('bookings')

        
        request.session['booking_date'] = booking_date
        request.session['start_time'] = start_time
        request.session['end_time'] = end_time

        return redirect('bookingSubmit')


    return render(request, 'enquiries.html', {
        'weekdsays':weekdays,
        'validateWeekdays':validateWeekdays,
    })

class BookingList(FormView):
    template_name ='user_booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = self.request.user.booking_set.all()
        return context


class BookingAmend(UpdateView):
    model = Booking
    template_name = 'amend_booking.html'
    fields = ['booking_date', 'start_time', 'end_time', 'address', 'dietary_requirements', 'booking_size']
    success_url ='/', 'user_booking.html'

    def get_queryset(self):
        return self.request.user.booking_set.all()


class BookingDelete(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url ='/', 'user_booking.html'

    def get_queryset(self):
        return self.request.user.booking_set.all()