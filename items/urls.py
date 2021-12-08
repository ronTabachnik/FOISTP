from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('items/<uuid:item_id>/', views.item_detail_view, name='item'),
]
