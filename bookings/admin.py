from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin

# Booking Model
admin.site.register(Booking)

