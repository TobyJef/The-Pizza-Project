from . import views
from django.urls import path
from .views import display_bookings


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),
    path('user_bookings/', display_bookings, name ='display_bookings'),

]