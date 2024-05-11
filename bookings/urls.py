from . import views
from django.urls import path
from .views import user_bookings
from .views import AddBooking



urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('profile/', views.profile, name='profile'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),
    path('', AddBooking.as_view(), name='add_booking'),
]