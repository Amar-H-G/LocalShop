from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from seller.models import *
from products.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
# from .models import customer_bag_items, CustomerRegistrationModel

from django.core.mail import send_mail

# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )



def indexView(request):
    logout(request)
    return render(request, 'index_customer.html')




def indexView_customer_login(request):
    user_id = request.session.get('user_id')  # Check if user is logged in
    username = None  # Initialize username to None
    print(user_id)
    
    if user_id:
        try:
            # Fetch user details based on user_id
            usermodel = CustomerRegistrationModel.objects.get(customer_id=user_id)
            username = usermodel.username  # Get the username of the logged-in user
        except CustomerRegistrationModel.DoesNotExist:
            # If user doesn't exist, clear the session
            request.session.flush()

    return render(request, 'index_customer_login.html', {'username': username,'user_id': user_id})


# @login_required
def clothes_shop(request, user_id, username):
    sellers = ClothesShopSeller.objects.all()
    return render (request,'clothes_customer_shops.html',{'sellers': sellers,'model_name': 'clothes','user_id': user_id, 'username': username})

# @login_required
def drinks_shop(request, user_id, username):
    sellers = DrinksShopSeller.objects.all()
    return render(request,'drinks_customer_shops.html',{'sellers': sellers, 'model_name': 'drinks', 'user_id': user_id, 'username': username})

# @login_required
def electronics_shop(request, user_id, username):
    sellers = ElectronicsShopSeller.objects.all()
    return render (request,'electronics_customer_shops.html',{'sellers': sellers, 'model_name': 'electronics','user_id': user_id, 'username': username})

# @login_required
def foods_shop(request, user_id, username):
    sellers = FoodsShopSeller.objects.all()
    return render (request,'foods_customer_shops.html',{'sellers': sellers, 'model_name': 'foods','user_id': user_id, 'username': username})

# @login_required
def fruits_shop(request, user_id, username):
    sellers = FruitsShopSeller.objects.all()
    return render (request,'fruits_customer_shops.html',{'sellers': sellers, 'model_name': 'fruits','user_id': user_id, 'username': username})

# @login_required
def grocery_shop(request, user_id, username):
    sellers = GroceryShopSeller.objects.all()
    return render (request,'grocery_customer_shops.html',{'sellers': sellers, 'model_name': 'grocery','user_id': user_id, 'username': username})

# @login_required
def house_shop(request, user_id, username):
    sellers = HouseComponentShopSeller.objects.all()
    return render (request,'house_customer_shops.html',{'sellers': sellers, 'model_name': 'house','user_id': user_id, 'username': username})

# @login_required
def icecream_shop(request, user_id, username):
    sellers = IceCreamShopSeller.objects.all()
    return render (request,'icecream_customer_shops.html',{'sellers': sellers, 'model_name': 'icecream','user_id': user_id, 'username': username})

# @login_required
def vegetables_shop(request, user_id, username):
    sellers = VegetablesShopSeller.objects.all()
    return render (request,'vegetables_customer_shops.html',{'sellers': sellers, 'model_name': 'vegetables','user_id': user_id, 'username': username})

# @login_required
def meat_shop(request, user_id, username):
    sellers = MeatShopSeller.objects.all()
    return render (request,'meat_customer_shops.html',{'sellers': sellers, 'model_name': 'meat','user_id': user_id, 'username': username})



#Items Added into the Bag

def add_to_bag(request, username, user_id, model_name, item_id):
    # Fetch the customer object (user)
    user = get_object_or_404(CustomerRegistrationModel, customer_id=user_id)
    
    # Fetch the product based on model_name and item_id
    if model_name == "drinks":
        product = get_object_or_404(DrinksProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(DrinksProducts)

    elif model_name == "electronics":
        product = get_object_or_404(ElectronicsProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(ElectronicsProducts)

    elif model_name == "clothes":
        product = get_object_or_404(ClothesProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(ClothesProducts)

    elif model_name == "icecream":
        product = get_object_or_404(IceCreamProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(IceCreamProducts)

    elif model_name == "vegetables":
        product = get_object_or_404(VegetablesProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(VegetablesProducts)

    elif model_name == "meat":
        product = get_object_or_404(MeatProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(MeatProducts)

    elif model_name == "house":
        product = get_object_or_404(HouseComponentProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(HouseComponentProducts)

    elif model_name == "grocery":
        product = get_object_or_404(GroceryProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(GroceryProducts)

    elif model_name == "fruits":
        product = get_object_or_404(FruitsProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(FruitsProducts)

    elif model_name == "foods":
        product = get_object_or_404(FoodsProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(FoodsProducts)

    else:
        # Handle other models or return an error page if invalid
        return redirect('error_page')  # Placeholder for error page

    # Handle the form submission (POST request)
    if request.method == "POST":
        # Create the item entry in the shopping bag model
        customer_bag_items.objects.create(
            customer_id=user,
            content_type=content_type,
            object_id=item_id,
            product=product,
            product_photo=product.product_photo,  # Assuming product has 'product_photo' field
            product_name=product.name,
            price=product.price
        )
        # After saving, you can either redirect to the same page or to another page (like the shopping bag)
        return redirect(request.META.get('HTTP_REFERER'))  # Redirect back to the page where the form was submitted

 # Show items into the htms page

def view_customer_bag(request, user_id,username):
    # Get the customer (user) object
    user = get_object_or_404(CustomerRegistrationModel, customer_id=user_id)

    # Fetch the items in the customer's shopping bag
    bag_items = customer_bag_items.objects.filter(customer_id=user)

    # Pass the bag items to the template
    return render(request, 'bag&whishlist/bag.html', {'bag_items': bag_items,'user_id': user_id, 'username': username})

#delete items from bag and whishlist
def delete_item_from_bag(request, user_id, order_id):
    # Get the customer (user) object
    user = get_object_or_404(CustomerRegistrationModel, customer_id=user_id)

    # Fetch the specific item in the customer's bag
    item = get_object_or_404(customer_bag_items, order_id=order_id, customer_id=user)

    # Delete the item from the shopping bag
    item.delete()

    # Redirect back to the shopping bag page (or wherever you'd like)
    return redirect(request.META.get('HTTP_REFERER'))


def delete_item_from_whishlist(request, user_id, order_id):
    # Get the customer (user) object
    user = get_object_or_404(CustomerRegistrationModel, customer_id=user_id)

    # Fetch the specific item in the customer's bag
    item = get_object_or_404(customer_whislist_items, order_id=order_id, customer_id=user)

    # Delete the item from the shopping bag
    item.delete()

    # Redirect back to the shopping bag page (or wherever you'd like)
    return redirect(request.META.get('HTTP_REFERER'))


def add_to_whishlist(request, username, user_id, model_name, item_id):
    # Fetch the customer object (user)
    user = get_object_or_404(CustomerRegistrationModel, customer_id=user_id)
    
    # Fetch the product based on model_name and item_id
    if model_name == "drinks":
        product = get_object_or_404(DrinksProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(DrinksProducts)

    elif model_name == "electronics":
        product = get_object_or_404(ElectronicsProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(ElectronicsProducts)

    elif model_name == "clothes":
        product = get_object_or_404(ClothesProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(ClothesProducts)

    elif model_name == "icecream":
        product = get_object_or_404(IceCreamProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(IceCreamProducts)

    elif model_name == "vegetables":
        product = get_object_or_404(VegetablesProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(VegetablesProducts)

    elif model_name == "meat":
        product = get_object_or_404(MeatProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(MeatProducts)

    elif model_name == "house":
        product = get_object_or_404(HouseComponentProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(HouseComponentProducts)

    elif model_name == "grocery":
        product = get_object_or_404(GroceryProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(GroceryProducts)

    elif model_name == "fruits":
        product = get_object_or_404(FruitsProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(FruitsProducts)

    elif model_name == "foods":
        product = get_object_or_404(FoodsProducts, id=item_id)
        content_type = ContentType.objects.get_for_model(FoodsProducts)

    else:
        # Handle other models or return an error page if invalid
        return redirect('error_page')  # Placeholder for error page

    # Handle the form submission (POST request)
    if request.method == "POST":
        # Create the item entry in the shopping bag model
        customer_whislist_items.objects.create(
            customer_id=user,
            content_type=content_type,
            object_id=item_id,
            product=product,
            product_photo=product.product_photo,  # Assuming product has 'product_photo' field
            product_name=product.name,
            price=product.price
        )
        # After saving, you can either redirect to the same page or to another page (like the shopping bag)
        return redirect(request.META.get('HTTP_REFERER'))  # Redirect back to the page where the form was submitted

# Show items into the htms page

def view_customer_whishlist(request, user_id,username):
    # Get the customer (user) object
    user = get_object_or_404(CustomerRegistrationModel, customer_id=user_id)

    # Fetch the items in the customer's shopping bag
    whish_items = customer_whislist_items.objects.filter(customer_id=user)

    # Pass the bag items to the template
    return render(request, 'bag&whishlist/whishlist.html', {'whish_items': whish_items,'user_id': user_id, 'username': username})