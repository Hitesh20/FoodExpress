from django.urls import path
from .views import my_restaurant_menu
urlpatterns = [
    path('my_restaurant_menu/', my_restaurant_menu, name='my_restaurant_view'),
]
