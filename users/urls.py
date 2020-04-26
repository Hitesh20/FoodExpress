from django.urls import path
from .views import register_restaurant_view, register_customer_view, login_user_view, logout_view
urlpatterns = [
    path('login/', login_user_view, name='login'),
    path('customer_registration/', register_customer_view, name='register_customer'),
    path('restaurant_registration/', register_restaurant_view, name='register_restaurant'),
    path('logout/', logout_view, name='logout'),
]