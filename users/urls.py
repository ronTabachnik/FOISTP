from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path("cart/", views.cart, name="cart")
]
