from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<uuid:item_id>/', views.item_detail, name='item'),
]
