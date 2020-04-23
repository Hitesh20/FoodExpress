from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .forms import RegisterRestaurant
from django.contrib import messages
from django.views.generic import CreateView


# Create your views here.

def my_restaurant_menu(request):
    # print("coming here")
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'restaurant/my_restaurant_menu.html')

def index_view(request):
    return render(request, 'restaurant/index.html')

def register_restaurant(request):
    if request.method == 'POST':
        form = RegisterRestaurant(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                username = request.POST.get('name')
                messages.success(request, f'{username}, Your account has been created! You are now able to login.')
                return redirect('/')
    else:
        # if request.POST.get('email') != Restaurant.objects.get(email=request.POST.get('email')):
        #     messages.warning(request, f'Account with this email id is already registered.')
        # else:
        #     messages.warning(request, f'Not able to create account for you. Please Try again.')
        form = RegisterRestaurant(request.POST)

    return render(request, 'restaurant/restaurant_registration.html', {'form': form})