from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('menu/', views.menu, name='menu'),
    # path('enquiries/', views.enquiries, name='enquiries'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_review'),
]