from django import forms
from .models import Restaurant
from django.contrib.auth.forms import UserCreationForm

class RegisterRestaurant(UserCreation Form):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'contact_no',
            'email',
            'password'
        ]