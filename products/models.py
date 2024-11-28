from django.db import models
from seller.models import *

# Create your models here.

class DrinksProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  Drink_Types = [
        ('A', 'Alcoholic'),
        ('N-A', 'Non-Alcoholic'),
    ]
  seller = models.ForeignKey(DrinksShopSeller, to_field='seller_id', on_delete=models.CASCADE, null=True)
  # print(seller)
  name=models.CharField(max_length=50)
  price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)  # Price per unit
  ingredients=models.CharField(max_length=50)
  drink_Type=models.CharField(max_length=3,choices=Drink_Types,default='N-A')
  variety=models.CharField(max_length=50)
  quantity=models.CharField(max_length=50)
  product_photo=models.ImageField(upload_to='photos/')
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')

  
class ElectronicsProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  choices=[
    ('y', 'yes'),
    ('N', 'No'),
  ]
  seller = models.ForeignKey(ElectronicsShopSeller, to_field='seller_id',  on_delete=models.CASCADE,null=True)
  name=models.CharField(max_length=50)
  price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)  # Price per unit
  brand = models.CharField(max_length=50)
  condition = models.CharField(max_length=50, blank=True, null=True)  # Optional condition
  battery_life = models.CharField(max_length=50, blank=True, null=True)  # Optional battery life
  display_type = models.CharField(max_length=50, blank=True, null=True)  # Optional display type (e.g., OLED, LCD)
  storage = models.CharField(max_length=100, blank=True, null=True)  # Optional storage details (e.g., 256GB SSD)
  processor = models.CharField(max_length=100, blank=True, null=True)
  memory = models.CharField(max_length=50, blank=True, null=True)
  operating_system = models.CharField(max_length=100, blank=True, null=True)
  Warrenty=models.CharField(max_length=2,choices=choices,default='N')
  product_photo=models.ImageField(upload_to='photos/')
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')
  

class FoodsProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  choices=[
    ('Bg', 'Bag'),
    ('J', 'Jar'),
    ('B', 'Box'),
    ('V', 'Vaccum Sealed'),
    ]
  seller = models.ForeignKey(FoodsShopSeller, to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100)
  Nutrations = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  packaging = models.CharField(max_length=100,choices=choices,default='Box')  # e.g., 'Box', 'Bag', 'Jar', 'Vacuum Sealed'
  product_photo=models.ImageField(upload_to='photos/')
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')

class FruitsProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
    ]
  
  seller = models.ForeignKey(FruitsShopSeller, to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100, blank=False)  # Name of the fruit
  price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)  # Price per unit
  # quantity = models.PositiveIntegerField(max_length=3,choices=Quantity,default='m')  # Available quantity in stock
  product_photo=models.ImageField(upload_to='photos/')
  created_at = models.DateTimeField(null=True, blank=True)  # Automatically set when the fruit is added
  # updated_at = models.DateTimeField(auto_now=True)  # Automatically set when the fruit is updated
  delivery=models.CharField(max_length=4,choices=Delivery)
  

class GroceryProducts(models.Model):
  
  Delivery=[
    ('Yes', 'yes'),
    ('N', 'No'),
  ]
  seller = models.ForeignKey(GroceryShopSeller,to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100, blank=False)  # Name of the grocery item
  price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)  # Price of the grocery item
  # quantity = models.PositiveIntegerField(max_length=3,choices=Quantity,default='m')  # Available quantity in stock
  # image = models.ImageField(upload_to='Grocery_images/', blank=False)  # Optional image for the clothing item
  product_photo=models.ImageField(upload_to='photos/')
  # created_at = models.DateTimeField(null=True, blank=True)
  # updated_at = models.DateTimeField(auto_now=True)
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')
  


class HouseComponentProducts(models.Model):
  Delivery=[('Yes', 'yes'),
    ('No', 'No'),]
  seller = models.ForeignKey(HouseComponentShopSeller, to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100)  # Name of the fruit
  price = models.DecimalField(max_digits=5, decimal_places=2)  # Price per unit
  product_photo=models.ImageField(upload_to='photos/')
  Size=models.CharField(max_length=50)
  product_type=models.CharField(max_length=50)
  # image = models.ImageField(upload_to='housecomponent_images/', blank=False)  # Optional image for the clothing item
  product_description=models.TextField(max_length=200)
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')



class IceCreamProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  seller = models.ForeignKey(IceCreamShopSeller,to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100)  # Name of the ice cream
  flavor = models.CharField(max_length=50)  # Flavor of the ice cream
  price = models.DecimalField(max_digits=5, decimal_places=2)  # Price of the ice cream
  size = models.CharField(max_length=20, choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])  # Size options
  stock = models.PositiveIntegerField()  # Quantity in stock
  product_photo= models.ImageField(upload_to='ice_cream_images/')  # Image of the ice cream
  description = models.TextField(blank=True, null=True)  # Optional description of the ice cream
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')
  

class VegetablesProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  seller = models.ForeignKey(VegetablesShopSeller, to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50)  # e.g., leafy, root, fruit, etc.
  quantity_available = models.PositiveIntegerField()  # How many items are available
  price = models.DecimalField(max_digits=7, decimal_places=2, default=True)  # Price for each unit of the vegetable
  description = models.TextField(blank=True, null=True)
  product_photo= models.ImageField(upload_to='vegetable_images/')  # Optional: image of the vegetable
  def __str__(self):
    return f"{self.name} ({self.seller.name})"
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')



class ClothesProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  seller = models.ForeignKey(ClothesShopSeller, to_field='seller_id', on_delete=models.CASCADE,null=True)
  # seller = models.ForeignKey(Seller, to_field='seller_id', on_delete=models.CASCADE, related_name='clothing_items')  # Relate item to seller
  name = models.CharField(max_length=100)  # Item name (e.g., T-shirt, Jeans)
  description = models.TextField()  # Detailed description
  category = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=True)  # Price of the item
  stock = models.PositiveIntegerField()  # Number of items available
  size = models.CharField(max_length=10, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')])
  color = models.CharField(max_length=50)  # Color of the item
  brand = models.CharField(max_length=50,null=True, blank=True)  # Optional field for brand
  product_photo= models.ImageField(upload_to='clothing_images/')  # Optional image for the clothing item
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')
  # created_at = created_at.isoformat()
    
  
class MeatProducts(models.Model):
  Delivery=[
    ('Yes', 'yes'),
    ('No', 'No'),
  ]
  seller = models.ForeignKey(MeatShopSeller, to_field='seller_id', on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100, default=True)
  product_type = models.CharField(max_length=50, choices=[('beef', 'Beef'), ('chicken', 'Chicken'), ('pork', 'Pork'), ('lamb', 'Lamb')], blank=False)
  weight = models.FloatField()  # Weight in kg
  price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
  stock = models.PositiveIntegerField()  # Available stock in kg
  # created_at = models.DateTimeField(null=True, blank=True)
  product_photo= models.ImageField(upload_to='meat_images/')  # Optional image for the clothing item
  delivery=models.CharField(max_length=4,choices=Delivery,default='Yes')
  

