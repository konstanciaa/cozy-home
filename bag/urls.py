from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('wishlist/', views.WishListView.as_view(), name='wishlist'),
    path('add-to-wishlist', views.add_to_wishlist, name='add-to-wishlist'),
    path('remove_from_wishlist', views.remove_from_wishlist,
         name='remove_from_wishlist'),
]
