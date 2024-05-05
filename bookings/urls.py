from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('enquiries/', views.enquiries, name='enquiries'),
    path('user_booking', views.user_booking, name='user_booking'),
    path('amend_booking/', views.booking_amend, name='booking_amend'),
    path('delete_booking/', views.booking_delete, name='booking_delete'),
]