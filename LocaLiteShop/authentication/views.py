from django.shortcuts import render,redirect
# from LocaLiteShop import authentication
from seller.models import *
from Localite.models import CustomerRegistrationModel
from .forms import LoginForm,RegistrationForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

#seller Register View

def register_seller(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            # Get the shop type and other form data
            seller_name = form.cleaned_data['seller_name']
            shop_name = form.cleaned_data['shop_name']
            shop_type = form.cleaned_data['shop_type']
            contact_number = form.cleaned_data['contact_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  # Store hashed password
            address = form.cleaned_data['address']
            opening_hours = form.cleaned_data['opening_hours']
            # created_at = form.cleaned_data['created_at']
            shop_Image = form.cleaned_data['shop_Image']

            # Hash the password using make_password
            hashed_password = make_password(password)
            
            # Depending on the shop_type, save the data in the respective model
            if shop_type == 'drink_shop':
                DrinksShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'electronics_shop':
                ElectronicsShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'fruit_shop':
                FruitsShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'food_shop':
                FoodsShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'grocery_shop':
                GroceryShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'house_component_shop':
                HouseComponentShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'icecream_shop':
                IceCreamShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'clothes_shop':
                ClothesShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'vegetable_shop':
                VegetablesShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            elif shop_type == 'meat_shop':
                MeatShopSeller.objects.create(seller_name=seller_name,shop_name=shop_name,shop_type=shop_type,contact_number=contact_number,email=email,password=hashed_password,address=address,opening_hours=opening_hours,shop_Image=shop_Image)
            
            subject = "Welcome to LocalShop"
            message = f"Hi {seller_name},\n\nThank you for registering at LocalShop. Your shop, '{shop_name}', is successfully registered under '{shop_type}'.\n\nBest regards,\nLocalShop Team"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)
            
            # Redirect to a success page
            return redirect('login_seller')
    else:
        form = RegistrationForm()

    return render(request, 'seller_registration.html', {'form': form})


#seller Login View

def login_seller(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            shop_type = form.cleaned_data['shop_type']  # The shop type selected by the user
            
            # Map shop types to their corresponding models
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
            
            # Get the model for the selected shop type
            model_class = shop_model_mapping.get(shop_type)
            if model_class:
                # Query the selected model by email
                sellers = model_class.objects.filter(email=email)
                if sellers.exists():
                    seller = sellers.first()  # Get the first matched seller
                    
                    # Check if the password matches
                    if check_password(password, seller.password):
                        request.session['shop_type'] = shop_type
                        request.session['seller_id'] = seller.seller_id

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
                        form.add_error('password', 'Invalid password')
                else:
                    form.add_error('email', 'User with this email does not exist')
            else:
                form.add_error('shop_type', 'Invalid shop type selected')
    else:
        form = LoginForm()

    return render(request, 'seller_login.html', {'form': form})


#seller Logout View

def logout_seller(request):
    if request.method=='POST':
        logout(request)
        return redirect('login_seller')



# Customer Registration

def CustomerRegistration(request):
    if request.method == 'POST':
        # Fetch data from the form
        username = request.POST.get('username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip')

        # Print the values to debug (you can remove this in production)
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"First Name: {fname}")
        print(f"City: {city}")
        print(f"Zip Code: {zip_code}")

        # Validation Checks
        if CustomerRegistrationModel.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists! Please try another Username')
            return redirect('register')

        if CustomerRegistrationModel.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exists! Please try another Email')
            return redirect('register')

        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('register')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, "Username must be Alphanumeric")
            return redirect('register')

        # Hash the password before saving
        password1 = make_password(pass1)

        try:
            # Create a new customer record
            customer = CustomerRegistrationModel.objects.create(
                username=username, 
                firstname=fname, 
                lastname=lname,
                email=email, 
                password=password1, 
                city=city, 
                zip=zip_code
            )

            subject = "Welcome to LocalShop"
            message = f"Hi {fname},\n\nThank you for registering at LocalShop. We’re excited to have you onboard!\n\nBest regards,\nLocalShop Team"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)
            # Success message after successful registration
            messages.success(request, "Your Account Has Been Created Successfully")
            return redirect('login')  # Redirect to login page

        except Exception as e:
            # Error handling (in case something goes wrong)
            messages.error(request, f"An error occurred while creating the account: {str(e)}")
            return redirect('register')

    # If not POST request, render the registration form
    return render(request, 'CustomerRegistration/Registration.html')




def UserLogin(request):
    if request.method == 'POST':
        # Fetch data from the form
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        try:
            # Check if the username exists in the CustomerRegistrationModel
            customer = CustomerRegistrationModel.objects.get(username=username)
            
            # Check if the password matches the stored hashed password
            if check_password(password, customer.password):
                # If credentials are correct, redirect to the home page or dashboard
                request.session['user_id'] = customer.customer_id
                messages.success(request, "You have successfully logged in.")
                return redirect('Index_login')  # Redirect to your home page or dashboard
            else:
                messages.error(request, "Invalid password. Please try again.")
                return redirect('login')  # Redirect back to the login page

        except CustomerRegistrationModel.DoesNotExist:
            # If the username doesn't exist, show an error
            messages.error(request, "Username does not exist. Please try again.")
            return redirect('login')  # Redirect back to the login page

    # If GET request, render the login page
    return render(request, 'CustomerRegistration/Login.html')


# Customer Login

def customer_logout_view(request):
    if 'user_id' in request.session:
    # and request.session['user_id'] == user_id:
        del request.session['user_id']  # Delete the user_id from the session
        logout(request)  # Log out the user session
        messages.success(request, "You have successfully logged out.")
        return redirect('Index')  # Redirect to the home or index page
    else:
        messages.error(request, "You are not logged in or session has expired.")
        return redirect('login')  # Redirect to login if not logged in or session mismatch