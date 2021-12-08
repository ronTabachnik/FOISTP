from django.urls import path
from . import views
# Ron, use this module ↓ to implement login+register+logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path("cart/", views.cart, name="cart")
]
