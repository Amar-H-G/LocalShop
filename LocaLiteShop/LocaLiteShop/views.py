from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from .forms import userRegistrationForm 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from Localite.models import CustomerRegistrationModel


def home(request):
  if 'user_id' in request.session:
        user = CustomerRegistrationModel.objects.get(customer_id=request.session['user_id'])
        return render(request, 'FirstHome.html', {'user': user})
  else:
      # logout(request)
      return render(request,'FirstHome.html')