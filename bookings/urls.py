from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),

]