from django.shortcuts import render,redirect,get_object_or_404
from seller.models import *
from products.models import *
from django.contrib.auth.decorators import login_required 

# Create your views here.


# @login_required
def drinks_customer_views(request, seller_id, user_id, username):
   # Get the seller by ID
    seller = get_object_or_404(DrinksShopSeller, seller_id=seller_id)
    # Get the products for this seller (assuming a ForeignKey relationship with seller)
    products = DrinksProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'drinks_customer_products.html',{'products': products, 'user_id': user_id, 'username': username})

# @login_required
def clothes_customer_views(request,seller_id, username, user_id):
    seller = get_object_or_404(ClothesShopSeller, id=seller_id)
    products = ClothesProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'clothes_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def fruits_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(FruitsShopSeller, id=seller_id)
    products = FruitsProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'fruits_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def foods_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(FoodsShopSeller, id=seller_id)
    products = FoodsProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'foods_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def grocery_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(GroceryShopSeller, id=seller_id)
    products = GroceryProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'grocery_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def housecomponent_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(HouseComponentShopSeller, id=seller_id)
    products = HouseComponentProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'house_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def icecream_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(IceCreamShopSeller, id=seller_id)
    products = IceCreamProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'icecream_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def meat_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(MeatShopSeller, seller_id=seller_id)
    products = MeatProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'meat_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def vegetables_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(VegetablesShopSeller, id=seller_id)
    products = VegetablesProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'vegetables_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

# @login_required
def electronics_customer_views(request,seller_id, user_id, username):
    seller = get_object_or_404(ElectronicsShopSeller, id=seller_id)
    products = ElectronicsProducts.objects.filter(seller_id=seller.seller_id)
    return render(request,'electronics_customer_products.html',{'products': products,'user_id': user_id, 'username': username})

