from django.urls import path
from . import views
# Ron, use this module ↓ to implement login+register+logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add_to_wishlist/<uuid:item_id>/',
         views.add_to_wishlist_view, name='add_to_wishlist'),
    path('remove_from_wishlist/<uuid:item_id>/',
         views.remove_from_wishlist_view, name='remove_from_wishlist'),
    path("cart/", views.cart, name="cart")
]
