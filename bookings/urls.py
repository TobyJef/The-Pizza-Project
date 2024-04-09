from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('', views.PostDetail.as_view(), name='menu'),
    path('', views.PostDetail.as_view(), name='enquiries'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_review'),
]