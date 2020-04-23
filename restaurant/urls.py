from django.urls import path
from .views import my_restaurant_menu, register_restaurant
urlpatterns = [
    path('my_restaurant_menu/', my_restaurant_menu, name='my_restaurant_view'),
    path('restaurant_registration/', register_restaurant, name='register_restaurant')
]
