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
    start_time = models.TimeField(auto_now_add=False, blank=False, null=True)
    end_time = models.TimeField(auto_now_add=False, blank=False, null=True)
    address = models.CharField(max_length=150)
    dietary_requirements = models.CharField(max_length=150, default="No Diertary Requirements/Allergies Stated")
    booking_size = models.PositiveIntegerField(null=True)
    requests = models.CharField(max_length=600, default="No Additional Request")
    approved = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user}. Date: {self.booking_date} | Start Time: {self.start_time} | End Time: {self.end_time} | Address: {self.address} | Booking Size: {self.booking_size}"