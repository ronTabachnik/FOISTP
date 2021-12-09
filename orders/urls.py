from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_view, name='orders'),
    path('<uuid:order_id>/', views.order_detail_view, name='order'),
    path('store/', views.store_orders_view, name='store_orders'),
    path('store/<uuid:order_id>/',
         views.store_order_detail_view, name='store_order'),
]
