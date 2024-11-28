from django.urls import path
from . import views


urlpatterns = [
  #  path('seller_home/', views.seller_home, name='seller_home'),
   path('item_add_view/', views.item_add_view, name='item_add_view'),
   path('<int:item_id>item_delete_view/', views.item_delete_view, name='item_delete_view'),
   path('drinks_seller_view/', views.drinks_seller_view, name='drinks_seller_view'),
   path('clothes_seller_view/', views.clothes_seller_view, name='clothes_seller_view'),
   path('Electronics_seller_view/', views.Electronics_seller_view, name='Electronics_seller_view'),
   path('foods_seller_view/', views.foods_seller_view, name='foods_seller_view'),
   path('fruit_seller_view/', views.fruit_seller_view, name='fruit_seller_view'),
   path('grocery_seller_view/', views.grocery_seller_view, name='grocery_seller_view'),
   path('HouseComponent_seller_view/', views.HouseComponent_seller_view, name='HouseComponent_seller_view'),
   path('iceCream_seller_view/', views.iceCream_seller_view, name='iceCream_seller_view'),
   path('meats_seller_view/', views.meats_seller_view, name='meats_seller_view'),
   path('vegetables_seller_view/', views.vegetables_seller_view, name='vegetables_seller_view'),
   ]
