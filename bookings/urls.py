from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('enquiries/', views.enquiries, name='enquiries'),
]