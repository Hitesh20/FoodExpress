from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .forms import RegisterRestaurant
from django.contrib import messages
from django.views.generic import CreateView


# Create your views here.

def my_restaurant_menu(request):
    return render(request, 'restaurant/my_restaurant_menu.html')

def index_view(request):
    return render(request, 'restaurant/index.html')

