from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

#Item Add View

# def item_add_view(request):
#     shop_type = request.session.get('shop_type', None)
#     seller_id = request.session.get('seller_id')

#     shop_type_mapping = {
#         'drink_shop': 'Drinks',
#         'electronics_shop': 'Electronics',
#         'fruit_shop': 'Fruits',
#         'food_shop': 'Foods',
#         'grocery_shop': 'Grocery',
#         'house_component_shop': 'HouseComponent',
#         'icecream_shop': 'IceCream',
#         'clothes_shop': 'Clothes',
#         'vegetable_shop': 'Vegetables',
#         'meat_shop': 'Meat',
#     }

#     model_shop_seller = {
#         'drink_shop': DrinksShopSeller,
#         'electronics_shop': ElectronicsShopSeller,
#         'fruit_shop': FruitsShopSeller,
#         'food_shop': FoodsShopSeller,
#         'grocery_shop': GroceryShopSeller,
#         'house_component_shop': HouseComponentShopSeller,
#         'icecream_shop': IceCreamShopSeller,
#         'clothes_shop': ClothesShopSeller,
#         'vegetable_shop': VegetablesShopSeller,
#         'meat_shop': MeatShopSeller,
#     }

#     condition = shop_type_mapping.get(shop_type)
#     shop_seller_model = model_shop_seller.get(shop_type)
    
#     if not condition:
#         return render(request, 'error_page.html', {'message': 'Invalid shop type'})
    
#     if request.method == 'POST':
#         form = item_add_form(request.POST, request.FILES, condition=condition)

#         if form.is_valid():
#             item = form.save(commit=False)
#             try:
#                 # Fetch the seller using seller_id
#                 seller = shop_seller_model.objects.get(seller_id=seller_id)  # Using seller_id as primary key
#                 item.seller = seller  # Assign seller instance to item
#             except shop_seller_model.DoesNotExist:
#                 return render(request, 'error_page.html', {'message': 'Seller not found.'})

#             item.save()

#             # Redirect based on shop type
#             redirect_mapping = {
#                 'drink_shop': 'drinks_seller_view',
#                 'electronics_shop': 'electronics_seller_view',
#                 'fruit_shop': 'fruit_seller_view',
#                 'food_shop': 'foods_seller_view',
#                 'grocery_shop': 'grocery_seller_view',
#                 'house_component_shop': 'house_component_seller_view',
#                 'icecream_shop': 'icecream_seller_view',
#                 'clothes_shop': 'clothes_seller_view',
#                 'vegetable_shop': 'vegetable_seller_view',
#                 'meat_shop': 'meat_seller_view',
#             }

#             redirect_view = redirect_mapping.get(shop_type)
#             if redirect_view:
#                 return redirect(redirect_view)
#             else:
#                 return render(request, 'error_page.html', {'message': 'Invalid shop type for redirection.'})
    
#     else:
#         form = item_add_form(request.POST, request.FILES, condition=condition)

#     seller_name = None
#     try:
#         # Get seller based on seller_id
#         seller = shop_seller_model.objects.get(seller_id=seller_id)  # Adjust based on primary key field
#         seller_name = seller.seller_name  # Adjust 'name' based on your model's field
#     except shop_seller_model.DoesNotExist:
#         seller_name = "Unknown Seller"

#     return render(request, 'item_add.html', {'form': form, 'seller_name': seller_name})


def item_add_view(request):
    shop_type = request.session.get('shop_type', None)
    seller_id = request.session.get('seller_id')
    shop_type_mapping={
        'drink_shop': 'Drinks',
        'electronics_shop': 'Electronics',
        'fruit_shop': 'Fruits',
        'food_shop': 'Foods',
        'grocery_shop': 'Grocery',
        'house_component_shop': 'HouseComponent',
        'icecream_shop': 'IceCream',
        'clothes_shop': 'Clothes',
        'vegetable_shop': 'Vegetables',
        'meat_shop': 'Meat',
}
    
    model_shop_seller = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }


    # Determine the condition based on shop_type
    condition = shop_type_mapping.get(shop_type)
    shop_seller_model=model_shop_seller.get(shop_type)
    if not condition:
        return render(request, 'error_page.html', {'message': 'Invalid shop type'})
    if request.method == 'POST':
        form = item_add_form(request.POST, request.FILES,condition=condition)
        # print(form.fields)
        if form.is_valid():
            item=form.save(commit=False)
            seller_id = request.session.get('seller_id')
            try:
                seller = shop_seller_model.objects.get(seller_id=seller_id)
                item.seller = seller  # Assign the actual seller instance
            except shop_seller_model.DoesNotExist:
                return render(request, 'error_page.html', {'message': 'Seller not found.'})

            item.save()
            if shop_type == 'drink_shop':
                return redirect('drinks_seller_view')  
                        
            elif shop_type == 'electronics_shop':
                return redirect('Electronics_seller_view')  
                        
            elif shop_type == 'fruit_shop':
                return redirect('fruit_seller_view')  
                        
            elif shop_type == 'food_shop':
                return redirect('foods_seller_view')  
                            
            elif shop_type == 'grocery_shop':
                return redirect('grocery_seller_view')  
                            
            elif shop_type == 'house_component_shop':
                return redirect('HouseComponent_seller_view')  
                            
            elif shop_type == 'icecream_shop':
                return redirect('iceCream_seller_view')    
                        
            elif shop_type == 'clothes_shop':
                return redirect('clothes_seller_view')
                        
            elif shop_type == 'vegetable_shop':
                return redirect('vegetables_seller_view')
                        
            elif shop_type == 'meat_shop':
                return redirect('meats_seller_view')

    else:
        form = item_add_form(request.POST, request.FILES, condition=condition)  # Print form validation errors
    
    seller_name = None
    try:
        seller = shop_seller_model.objects.get(seller_id=seller_id)
        seller_name = seller.seller_name  # Adjust 'name' based on your model's field
    except shop_seller_model.DoesNotExist:
        seller_name = "Unknown Seller"

    return render(request, 'item_add.html', {'form': form, 'seller_name': seller_name})

#Item Delete Form

def item_delete_view(request, item_id):
    # Retrieve shop_type from session
    shop_type = request.session.get('shop_type', None)
    seller_id = request.session.get('seller_id')
    # Map shop types to their corresponding product models
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    # Get the appropriate model for the current shop type
    model_class = product_model_mapping.get(shop_type)
    if not model_class:
        return render(request, 'error_page.html', {'message': 'Invalid shop type'})

    # Retrieve the seller ID from session to ensure deletion only happens for the authenticated seller's item
    # seller_id = request.session.get('seller_id')
    item = get_object_or_404(model_class, seller_id=seller_id, id=item_id)  # Ensure the item belongs to the logged-in seller

    # Perform the deletion
    if request.method == 'POST':
        item.delete()
        # Redirect based on shop type
        if shop_type == 'drink_shop':
            return redirect('drinks_seller_view')
        elif shop_type == 'electronics_shop':
            return redirect('Electronics_seller_view')
        elif shop_type == 'fruit_shop':
            return redirect('fruit_seller_view')
        elif shop_type == 'food_shop':
            return redirect('foods_seller_view')
        elif shop_type == 'grocery_shop':
            return redirect('grocery_seller_view')
        elif shop_type == 'house_component_shop':
            return redirect('HouseComponent_seller_view')
        elif shop_type == 'icecream_shop':
            return redirect('iceCream_seller_view')
        elif shop_type == 'clothes_shop':
            return redirect('clothes_seller_view')
        elif shop_type == 'vegetable_shop':
            return redirect('vegetables_seller_view')
        elif shop_type == 'meat_shop':
            return redirect('meats_seller_view')

    # Render a confirmation page (optional)
    model_shop_seller = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }

    # Retrieve seller name (optional)
    seller_name = None
    shop_seller_model = model_shop_seller.get(shop_type)
    if shop_seller_model:
        try:
            seller = shop_seller_model.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Adjust field name as needed
        except shop_seller_model.DoesNotExist:
            seller_name = "Unknown Seller"

    # Render a confirmation page (if applicable)
    return render(request, 'delete1.html', {'item': item, 'seller_name': seller_name})



#Item Views


def drinks_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        # Modify the query based on primary key configuration
        products = model_class.objects.filter(seller__seller_id=seller_id)  # Adjust if needed
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            # Use the correct lookup for fetching the seller
            seller = seller_model_class.objects.get(seller_id=seller_id)  # Adjust based on primary key field
            seller_name = seller.seller_name
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'Drinks.html', {'products': products, 'seller_name': seller_name})


# @login_required
def clothes_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'clothes.html', {'products': products, 'seller_name': seller_name})

# @login_required
def Electronics_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller__id=seller_id)
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'Electronics.html', {'products': products, 'seller_name': seller_name})

# @login_required
def foods_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'foods.html', {'products': products, 'seller_name': seller_name})
# @login_required
def fruit_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'fruit.html', {'products': products, 'seller_name': seller_name})

# @login_required
def grocery_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

        shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'grocery.html', {'products': products, 'seller_name': seller_name})

# @login_required
def HouseComponent_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

        shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'HouseComponents.html', {'products': products, 'seller_name': seller_name})


# @login_required
def iceCream_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'IceCreame.html', {'products': products, 'seller_name': seller_name})



def meats_seller_view(request):
    # Retrieve session data
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')

    # Define mappings for product models and seller models based on shop type
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }

    # Get the correct product model based on shop type
    model_class = product_model_mapping.get(shop_type)
    if model_class:
        # Filter products for the given seller_id
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []

    # Get the correct seller model based on shop type and fetch seller details
    seller_name = "Unknown Seller"  # Default name if seller not found
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            # Retrieve seller by seller_id
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming 'seller_name' is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"



    # Render the template with product and seller details
    return render(request, 'Meat.html', {'products': products, 'seller_name': seller_name})
# @login_required
def vegetables_seller_view(request):
    shop_type = request.session.get('shop_type')
    seller_id = request.session.get('seller_id')
    
    product_model_mapping = {
        'drink_shop': DrinksProducts,
        'electronics_shop': ElectronicsProducts,
        'fruit_shop': FruitsProducts,
        'food_shop': FoodsProducts,
        'grocery_shop': GroceryProducts,
        'house_component_shop': HouseComponentProducts,
        'icecream_shop': IceCreamProducts,
        'clothes_shop': ClothesProducts,
        'vegetable_shop': VegetablesProducts,
        'meat_shop': MeatProducts,
    }

    model_class = product_model_mapping.get(shop_type)
    if model_class:
        products = model_class.objects.filter(seller_id=seller_id)
    else:
        products = []  

    shop_model_mapping = {
        'drink_shop': DrinksShopSeller,
        'electronics_shop': ElectronicsShopSeller,
        'fruit_shop': FruitsShopSeller,
        'food_shop': FoodsShopSeller,
        'grocery_shop': GroceryShopSeller,
        'house_component_shop': HouseComponentShopSeller,
        'icecream_shop': IceCreamShopSeller,
        'clothes_shop': ClothesShopSeller,
        'vegetable_shop': VegetablesShopSeller,
        'meat_shop': MeatShopSeller,
    }
    
    seller_name = None
    seller_model_class = shop_model_mapping.get(shop_type)
    if seller_model_class:
        try:
            seller = seller_model_class.objects.get(seller_id=seller_id)
            seller_name = seller.seller_name  # Assuming `name` is a field in the seller model
        except seller_model_class.DoesNotExist:
            seller_name = "Unknown Seller"

    return render(request, 'vegetables.html', {'products': products, 'seller_name': seller_name})
