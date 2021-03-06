from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<uuid:category_id>',
         views.filter_by_category_view, name='category'),
    path('items/<uuid:item_id>/', views.item_detail_view, name='item'),
    path('review/<uuid:item_id>/', views.review_view, name='review'),
]
