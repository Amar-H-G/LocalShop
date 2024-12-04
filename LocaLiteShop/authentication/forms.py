from django import forms
from .models import *



#Seller Registration Form

class RegistrationForm(forms.Form):
    SHOP_TYPES = [
        ('meat_shop', 'Meat Shop'),
        ('fruit_shop', 'Fruit Shop'),
        ('food_shop', 'Food Shop'),
        ('drink_shop', 'Drink Shop'),
        ('electronics_shop', 'Electronics Shop'),
        ('grocery_shop', 'Grocery Shop'),
        ('house_component_shop', 'House Component Shop'),
        ('icecream_shop', 'Ice Cream Shop'),
        ('clothes_shop', 'Clothes Shop'),
        ('vegetable_shop', 'Vegetable Shop'),
    ]
    seller_name = forms.CharField(max_length=100, required=True)
    shop_name = forms.CharField(max_length=100, required=True)
    shop_type = forms.ChoiceField(choices=SHOP_TYPES, required=True)
    contact_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(max_length=255, required=True)  
    confirm_password = forms.CharField(max_length=255, required=True)  
    address = forms.CharField(max_length=500, required=False)  # Removed blank=True
    opening_hours = forms.CharField(max_length=50, required=False)  # Removed blank=True
    created_at = forms.DateTimeField()
    shop_Image = forms.ImageField(required=True)  # No blank=True needed

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


#Seller Login Form

class LoginForm(forms.Form):
    shop_type_choices = [
        ('drink_shop', 'Drink Shop'),
        ('electronics_shop', 'Electronics Shop'),
        ('fruit_shop', 'Fruit Shop'),
        ('food_shop', 'Food Shop'),
        ('grocery_shop', 'Grocery Shop'),
        ('house_component_shop', 'House Component Shop'),
        ('icecream_shop', 'Ice Cream Shop'),
        ('clothes_shop', 'Clothes Shop'),
        ('vegetable_shop', 'Vegetable Shop'),
        ('meat_shop', 'Meat Shop'),
    ]
    shop_type = forms.ChoiceField(choices=shop_type_choices,required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
