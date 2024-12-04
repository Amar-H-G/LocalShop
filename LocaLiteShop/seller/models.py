from django.db import models


# Create your models here.
class DrinksShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    def __str__(self):
        return self.shop_name
    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = DrinksShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)



class ElectronicsShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = ElectronicsShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

class FoodsShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = FoodsShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class FruitsShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = FruitsShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class GroceryShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = GroceryShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class HouseComponentShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = HouseComponentShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class IceCreamShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = IceCreamShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class VegetablesShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = VegetablesShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class ClothesShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = ClothesShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)


class MeatShopSeller(models.Model):
    seller_id = models.IntegerField(primary_key=True,default=0)
    seller_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_type = models.CharField(max_length=100)  # Add max_length for CharField
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)  # Store hashed password
    address = models.CharField(max_length=500, blank=True)  # Optional address
    opening_hours = models.CharField(max_length=50, blank=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    shop_Image = models.ImageField(upload_to='photos/')  # No need for blank=False
    # created_at = created_at.isoformat()
    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        if not self.seller_id:
            # Logic to determine the next ID, e.g., find the maximum + 1, or reset
            max_id = MeatShopSeller.objects.aggregate(models.Max('seller_id'))['seller_id__max']
            self.seller_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

