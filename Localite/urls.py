from django.urls import path
from . import views


urlpatterns = [
    #Customer Pages
    path('Index/',views.indexView,name='Index'),
    path('Index_login/',views.indexView_customer_login,name='Index_login'),
    path('clothes_shop/<int:user_id>/<str:username>/',views.clothes_shop,name='clothes_shop'),
    path('drinks_shop/<int:user_id>/<str:username>/',views.drinks_shop,name='drinks_shop'),
    path('electronics_shop/<int:user_id>/<str:username>/',views.electronics_shop,name='electronics_shop'),
    path('foods_shop/<int:user_id>/<str:username>/',views.foods_shop,name='foods_shop'),
    path('fruits_shop/<int:user_id>/<str:username>/',views.fruits_shop,name='fruits_shop'),
    path('grocery_shop/<int:user_id>/<str:username>/',views.grocery_shop,name='grocery_shop'),
    path('house_shop/<int:user_id>/<str:username>/',views.house_shop,name='house_shop'),
    path('icecream_shop/<int:user_id>/<str:username>/',views.icecream_shop,name='icecream_shop'),
    path('vegetables_shop/<int:user_id>/<str:username>/',views.vegetables_shop,name='vegetables_shop'),
    path('meat_shop/<int:user_id>/<str:username>/',views.meat_shop,name='meat_shop'),

    path('add-to-bag/<int:user_id>/<str:username>/<str:model_name>/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('view_customer_bag/<int:user_id>/<str:username>/', views.view_customer_bag, name='view_customer_bag'),

    path('add_to_whishlist/<int:user_id>/<str:username>/<str:model_name>/<int:item_id>/', views.add_to_whishlist, name='add_to_whishlist'),
    path('view_customer_whishlist/<int:user_id>/<str:username>/', views.view_customer_whishlist, name='view_customer_whishlist'),
    

    path('delete_item_from_bag/<int:user_id>/<int:order_id>/', views.delete_item_from_bag, name='delete_item_from_bag'),
    path('delete_item_from_whishlist/<int:user_id>/<int:order_id>/', views.delete_item_from_whishlist, name='delete_item_from_whishlist'),

]
