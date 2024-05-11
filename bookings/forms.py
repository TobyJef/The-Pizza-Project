from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    """" Form to create a booking """
    class Meta:
        model = Booking
        fields = ['title', 'first_name', 'last_name', 'email', 'phone_number','booking_date',
         'start_time', 'end_time', 'address', 'dietary_requirements', 'booking_size', 'requests']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control'}),
            'booking_date' : forms.TextInput(attrs={'class':'form-control'}),
            'start_time' : forms.TextInput(attrs={'class':'form-control'}),
            'end_time' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'dietary_requirements' : forms.TextInput(attrs={'class':'form-control'}),
            'booking_size' : forms.TextInput(attrs={'class':'form-control'}),
            'requests' : forms.TextInput(attrs={'class':'form-control'}),
        }

    labels = {
        'title' : 'Title',
        'first_name' : 'First Name',
        'last_name' : 'Last Name',
        'email' : 'Email',
        'phone_number' : 'Phone Number',
        'booking_date' : 'Booking Date',
        'start_time' : 'Start Time',
        'end_time' : 'End Time',
        'address' : 'Address',
        'dietary_requirements' : 'Dietary Requirements',
        'booking_size' : 'Booking Size',
        'requests' : 'Requests'
    }

class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
