from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Customer Booking Model

class Booking(models.Model):

    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=25)
    booking_date = models.DateField(null=True, auto_now=False, max_length=8)
    booking_time = models.TimeField(max_length=4, null=True)
    address = models.CharField(max_length=150)
    allergies = models.CharField(max_length=150, default="No Allergies Stated")
    booking_size = models.IntegerField(null=True)
    additional_requests = models.CharField(max_length=600, default="No Additional Request")