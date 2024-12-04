from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(DrinksProducts)
class DrinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'drink_Type', 'variety', 'quantity', 'delivery')
    search_fields = ('name', 'drink_Type')

# Register Electronics model
@admin.register(ElectronicsProducts)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'condition', 'delivery', 'Warrenty')
    search_fields = ('name', 'brand')
    list_filter = ('delivery', 'Warrenty')

# Register Foods model
@admin.register(FoodsProducts)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'packaging', 'delivery')
    search_fields = ('name',)
    list_filter = ('packaging', 'delivery')

# Register Fruits model
@admin.register(FruitsProducts)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'delivery')
    search_fields = ('name',)
    list_filter = ('delivery',)

# Register Grocery model
@admin.register(GroceryProducts)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',  'delivery')
    search_fields = ('name',)
    list_filter = ('delivery',)

# Register HouseComponent model
@admin.register(HouseComponentProducts)
class HouseComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'Size', 'product_type', 'delivery')
    search_fields = ('name', 'product_type')
    list_filter = ('delivery',)

# Register IceCream model
@admin.register(IceCreamProducts)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor', 'price', 'size', 'stock', 'delivery')
    search_fields = ('name', 'flavor')
    list_filter = ('size', 'delivery')

# Register Vegetables model
@admin.register(VegetablesProducts)
class VegetablesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity_available', 'price', 'delivery')
    search_fields = ('name', 'category')
    list_filter = ('category', 'delivery')

# Register Clothes model
@admin.register(ClothesProducts)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'size', 'color', 'delivery')
    search_fields = ('name', 'category', 'brand')
    list_filter = ('category', 'size', 'color', 'delivery')

# Register Meat model
@admin.register(MeatProducts)
class MeatAdmin(admin.ModelAdmin):
    list_display = ('name','product_type', 'weight', 'stock','price', 'delivery')
    search_fields = ('product_name', 'product_type')
    list_filter = ('product_type', 'delivery')
