from django import forms
from .models import *


class item_add_form(forms.ModelForm):
    class Meta:
        model = None  # Placeholder; will be set dynamically
        fields = []  # Will be set dynamically

    def __init__(self, *args, **kwargs):
        condition = kwargs.pop('condition', None)  # Retrieve the 'condition' argument

        # Conditional logic to set the model and fields
        if condition == 'Drinks':
            self._meta.model = DrinksProducts
            self._meta.fields = ['name', 'ingredients', 'price', 'drink_Type', 'variety', 'quantity', 'delivery', 'product_photo']
        elif condition == 'Foods':
            self._meta.model = FoodsProducts
            self._meta.fields = ['name', 'Nutrations', 'price', 'packaging', 'delivery', 'product_photo']
        elif condition == 'HouseComponent':
            self._meta.model = HouseComponentProducts
            self._meta.fields = ['name', 'price', 'Size', 'product_type', 'product_description', 'delivery', 'product_photo']
        elif condition == 'Electronics':
            self._meta.model = ElectronicsProducts
            self._meta.fields = ['name', 'price', 'brand', 'condition', 'battery_life', 'display_type', 'storage', 'processor', 'memory', 'operating_system', 'Warrenty', 'delivery', 'product_photo']
        elif condition == 'Fruits':
            self._meta.model = FruitsProducts
            self._meta.fields = ['name', 'price',  'delivery', 'product_photo']
        elif condition == 'Grocery':
            self._meta.model = GroceryProducts
            self._meta.fields = ['name', 'price',  'delivery', 'product_photo']
        elif condition == 'IceCream':
            self._meta.model = IceCreamProducts
            self._meta.fields = ['name', 'flavor', 'price', 'size', 'stock', 'description', 'delivery', 'product_photo']
        elif condition == 'Clothes':
            self._meta.model = ClothesProducts
            self._meta.fields = ['name', 'description', 'category', 'price', 'stock', 'size', 'color', 'brand',  'delivery', 'product_photo']
        elif condition == 'Meat':
            self._meta.model = MeatProducts
            self._meta.fields = ['name', 'product_type', 'weight', 'price', 'stock',  'delivery', 'product_photo']
        elif condition == 'Vegetables':
            self._meta.model = VegetablesProducts
            self._meta.fields = ['name', 'category', 'quantity_available', 'price', 'description',  'delivery', 'product_photo']
        else:
            raise ValueError("Invalid condition specified for the form.")
        
        super().__init__(*args, **kwargs)

        # Dynamically handle fields based on type
        for field_name in self._meta.fields:
            field = self._meta.model._meta.get_field(field_name)
            is_required = not field.blank  # Check if 'blank=False' on the model field
            
            if field.is_relation:
                self.fields[field_name] = forms.ModelChoiceField(
                    queryset=field.related_model.objects.all(),
                    required=is_required
                )
            elif isinstance(field, models.ImageField):  # Check if the field is an ImageField
                self.fields[field_name] = forms.ImageField(required=is_required)
            elif isinstance(field, models.CharField) and field.choices:  # Check for choice fields
                self.fields[field_name] = forms.ChoiceField(
                    choices=field.choices,
                    required=is_required
                )
            else:
                # Use CharField (or appropriate field type) based on the model field type
                self.fields[field_name] = forms.CharField(
                    initial=field.default if field.has_default() else None,
                    required=is_required
                )