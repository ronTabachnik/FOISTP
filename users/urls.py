from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
