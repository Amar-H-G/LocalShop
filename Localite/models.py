from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class CustomerRegistrationModel(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)  # Add max_length for CharField
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=100,null=False)  # Store hashed password
    # pass2 = models.CharField(max_length=100)
    city = models.CharField(max_length=500, blank=True)  # Optional address
    zip = models.CharField(max_length=50, blank=True)  # Optional
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.username})"
    


class customer_bag_items(models.Model):
    customer_id=models.ForeignKey(CustomerRegistrationModel, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Reference to product type
    object_id = models.PositiveIntegerField()  # ID of the referenced product
    product = GenericForeignKey('content_type', 'object_id')  # Dynamic reference to the product
    product_photo=models.ImageField(upload_to='photos/')
    product_name = models.CharField(max_length=255)
    # quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return f"Order {self.order_id} by {self.customer_id.username}"
    

class customer_whislist_items(models.Model):
    customer_id=models.ForeignKey(CustomerRegistrationModel, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Reference to product type
    object_id = models.PositiveIntegerField()  # ID of the referenced product
    product = GenericForeignKey('content_type', 'object_id')  # Dynamic reference to the product
    product_photo=models.ImageField(upload_to='photos/')
    product_name = models.CharField(max_length=255)
    # quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return f"Order {self.order_id} by {self.customer_id.username}"