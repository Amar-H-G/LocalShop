from django.contrib import admin
from .models import CustomerRegistrationModel,customer_bag_items,customer_whislist_items
# Register your models here.

@admin.register(CustomerRegistrationModel)
class CustomerRegistration(admin.ModelAdmin):
    list_display = ('customer_id','username','firstname','lastname', 'email', 'password', 'city', 'zip',)  # Fields to display in the list view
    list_filter = ('created_at',)  # Add filters for created_at field
    search_fields = ('username', 'email', 'zip')  # Add search functionality
    ordering = ('-created_at',)  # Order the list by created_at in descending order


@admin.register(customer_bag_items)
class CustomerBag(admin.ModelAdmin):
    list_display = ('customer_id','order_id','content_type','object_id', 'product_photo', 'product_name', 'price', 'order_date',)  # Fields to display in the list view
    list_filter = ('order_date',)  # Add filters for created_at field
    search_fields = ('product_name', 'object_id', 'price')  # Add search functionality
    ordering = ('-product_name',)  # Order the list by created_at in descending order


@admin.register(customer_whislist_items)
class CustomerWhishlist(admin.ModelAdmin):
    list_display = ('customer_id','order_id','content_type','object_id', 'product_photo', 'product_name', 'price', 'order_date',)  # Fields to display in the list view
    list_filter = ('order_date',)  # Add filters for created_at field
    search_fields = ('product_name', 'object_id', 'price')  # Add search functionality
    ordering = ('-product_name',)  # Order the list by created_at in descending order