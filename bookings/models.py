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




# Customer Booking Model

class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=10, choices=Title, blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=25)
    booking_date = models.DateField(null=True, auto_now=False, max_length=8)
    booking_time = models.TimeField(max_length=4, null=True)
    address = models.CharField(max_length=150)
    dietary_requirements = models.CharField(max_length=150, default="No Dietary Requirements/Allergies Stated")
    booking_size = models.IntegerField(null=True)
    requests = models.CharField(max_length=600, default="No Additional Request")
    def __str__(self):
        return f"{self.user.username} | booking_date: {self.booking_date} | time: {self.booking_time}"