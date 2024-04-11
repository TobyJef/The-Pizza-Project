from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Customer Booking Model

class Booking(models.Model):

    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField(null=True)
    booking_date = models.DateField(max_length=8)
    booking_time = models.TimeField(max_length=4)
    address = models.CharField(max_length=150)
    allergies = models.CharField(max_length=150)