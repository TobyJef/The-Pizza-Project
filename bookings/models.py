from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


Title = (
    ("Mr", "Mr"),
    ("Mrs", "Mrs"),
    ("Miss", "Miss"),
    ("Ms", "Ms"),
    ("Dr", "Dr"),
    ("Prof", "Prof"),
    ("Rev'd", "Rev'd"),
)

Time_Slots = (
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"), 
)


class Booking(models.Model):
    """ A model to create and manage customer bookings """
    user = models.ForeignKey(User, related_name='booking_maker', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=10, choices=Title, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=25)
    booking_date = models.DateField(null=True, auto_now=False, max_length=8)
    start_time = models.TimeField(auto_now_add=False, choices=Time_Slots, blank=False, null=True)
    end_time = models.TimeField(auto_now_add=False, choices=Time_Slots, blank=False, null=True)
    address = models.CharField(max_length=150)
    dietary_requirements = models.CharField(max_length=150, default="No Diertary Requirements/Allergies Stated")
    booking_size = models.PositiveIntegerField(null=True)
    requests = models.CharField(max_length=600, default="No Additional Request")
    approved = models.BooleanField(default=True)
    
    