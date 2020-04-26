from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class register_restaurant_form(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150, help_text='Email')
    contact_no = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'contact_no', 'password1', 'password2')


class register_customer_form(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150, help_text='Email')
    contact_no = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'contact_no', 'password1', 'password2')