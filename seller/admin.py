from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(DrinksShopSeller)
class DrinkSShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order
    
@admin.register(ElectronicsShopSeller)
class ElectronicsShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order
@admin.register(FoodsShopSeller)
class FoodsShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order
@admin.register(FruitsShopSeller)
class FruitsShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order
@admin.register(GroceryShopSeller)
class GroceryShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email' ,'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order
@admin.register(HouseComponentShopSeller)
class HouseComponentsShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order
@admin.register(IceCreamShopSeller)
class IceCreamShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order

@admin.register(VegetablesShopSeller)
class VegetablesShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order

@admin.register(ClothesShopSeller)
class ClothesShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order

@admin.register(MeatShopSeller)
class MeatShopSellers(admin.ModelAdmin):
    list_display = ('seller_name','shop_type','shop_name', 'contact_number', 'email', 'password','created_at','shop_Image')  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('seller_name', 'shop_name', 'email')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order