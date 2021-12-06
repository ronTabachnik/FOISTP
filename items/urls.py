from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/<str:item>', views.item_detail, name='item'),
]
