from django.urls import path
from . import views


urlpatterns = [
    #seller forms
    path('register_seller/',views.register_seller,name='register_seller'),
    path('seller_login/', views.login_seller, name='login_seller'),
    path('logout_seller/', views.logout_seller, name='logout_seller'),
    #Customer Forms
    path('register/', views.CustomerRegistration, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('logout', views.customer_logout_view, name='logout'),

]
