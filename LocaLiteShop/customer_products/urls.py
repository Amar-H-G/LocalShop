from django.urls import path
from . import views


urlpatterns = [
    
    path('drinks_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.drinks_customer_views,name='drinks_customer_views'),
    path('clothes_customer_views/<int:seller_id>/<str:username>/<int:user_id>/', views.clothes_customer_views,name='clothes_customer_views'),
    path('fruits_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.fruits_customer_views,name='fruits_customer_views'),
    path('foods_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.foods_customer_views,name='foods_customer_views'),
    path('grocery_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.grocery_customer_views,name='grocery_customer_views'),
    path('housecomponent_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.housecomponent_customer_views,name='housecomponent_customer_views'),
    path('icecream_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.icecream_customer_views,name='icecream_customer_views'),
    path('meat_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.meat_customer_views,name='meat_customer_views'),
    path('vegetables_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.vegetables_customer_views,name='vegetables_customer_views'),
    path('electronics_customer_views/<int:seller_id>/<str:username>/<int:user_id>', views.electronics_customer_views,name='electronics_customer_views'),

]