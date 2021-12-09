from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_view, name='orders'),
    path('<uuid:order_id>/', views.order_detail_view, name='order'),
]
