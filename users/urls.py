from django.urls import path
from . import views
# Ron, use this module ↓ to implement login+register+logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register-business/', views.register_as_business_view,
         name='register_business'),
    # NEEDS TO CREATE path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('change_status/<uuid:user_id>',
         views.change_profile_status_view, name='change_status'),
    # accept
    # reject business
    path('store_closure/', views.request_store_closure_view, name='store_closure'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add_to_wishlist/<uuid:item_id>/',
         views.add_to_wishlist_view, name='add_to_wishlist'),
    path('remove_from_wishlist/<uuid:item_id>/',
         views.remove_from_wishlist_view, name='remove_from_wishlist'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<uuid:item_id>/',
         views.add_to_cart_view, name='add_to_cart'),
    path('increase_item_quantity/<uuid:item_id>/',
         views.increase_item_amount_view, name="increase_amount"),
    path('decrease_item_quantity/<uuid:item_id>/',
         views.decrease_item_amount_view, name="decrease_amount"),
    path('remove_from_cart/<uuid:item_id>/',
         views.remove_from_cart_view, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('payment/', views.payment_view, name='payment'),
    path('store-dashboard/', views.store_dashboard_view, name='store dashboard')
]
