from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribers/', views.subscribers, name='subscribers'),
]
