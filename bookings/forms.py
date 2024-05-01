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
        booking_time = forms.TimeField(max_length=4, null=True)
        address = forms.CharField(widget=forms.Textarea, max_length=150)
        allergies = forms.CharField(widget=forms.Textarea, max_length=150, default="No Allergies Stated")
        booking_size = forms.IntegerField(null=True)
        additional_requests = forms.CharField(widget=forms.Textarea, max_length=300, default="No Additional Request")