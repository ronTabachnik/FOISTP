from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_return_requests_view, name='return_requests'),
    path('', views.return_request_view, name='return_request')
]
