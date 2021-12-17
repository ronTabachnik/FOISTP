from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:order_id>/<uuid:item>/<int:amount>/', views.crete_return_request_view,
         name='create return request'),
    path('store/', views.list_return_requests_view, name='store return requests'),
    path('store/<uuid:request_id>/', views.return_request_view,
         name='store return request'),
    path('store/accept_request/<uuid:request_id>',
         views.return_request_accept_view, name='store return request accept'),
    path('store/reject_request/<uuid:request_id>',
         views.return_request_reject_view, name='store return request reject'),
]
