from .models import Booking
from django import forms

# Customer Booking Form

class BookingForm(forms.Form):
    class Meta:
        model = Booking
        title = forms.CharField(max_length=10)
        first_name = forms.CharField(max_length=25)
        last_name = forms.CharField(max_length=25)
        email = forms.EmailField()
        phone_number = forms.IntegerField(null=True)
        booking_date = forms.DateField(null=True, auto_now=False, max_length=8)
        start_time = models.TimeField(auto_now_add=False, blank=False, null=True)
        end_time = models.TimeField(auto_now_add=False, blank=False, null=True)
        address = forms.CharField(widget=forms.Textarea, max_length=150)
        dietary_requirements = forms.CharField(widget=forms.Textarea, max_length=150, default="No Allergies Stated")
        booking_size = forms.IntegerField(null=True)
        requests = forms.CharField(widget=forms.Textarea, max_length=300, default="No Additional Request")


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
