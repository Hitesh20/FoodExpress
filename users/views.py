from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import register_customer_form, register_restaurant_form
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register_restaurant_view(request):
    form = register_restaurant_form(request.POST)
    if form.is_valid():
        u_name = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        print(form.cleaned_data)
        profile_object = Profile.objects.filter(email__exact=email)
        print(profile_object)
        flag = False
        for i in profile_object:
            if(i[email]==email):
                flag = True
        flag2 = False
        for i in User.objects.filter(username__iexact=u_name):
            if(i.username==u_name):
                flag2=True
        if flag:
            print('Email taken already.')
            messages.info(request, 'Email taken already.')
            form = register_restaurant_form()

        elif flag2:
            print('User Name Aready Taken')
            messages(request, 'User Name Aready Taken')
            form = register_restaurant_form()

        elif form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
            print('Password did not match.')
            messages(request, 'Password did not match.')
            form = register_restaurant_form()

        else:
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.contact_no = form.cleaned_data.get('contact_no')
            user.profile.is_restaurant = True
            user.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('index')
    else:
        form = register_restaurant_form()
    return render(request, 'users/restaurant_registration.html', {'form': form})



def register_customer_view(request):
    form = register_customer_form(request.POST)
    if form.is_valid():
        u_name = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        print(form.cleaned_data)
        profile_object = Profile.objects.filter(email__exact=email)
        print(profile_object)
        flag = False
        for i in profile_object:
            if(i[email]==email):
                flag = True
        flag2 = False
        for i in User.objects.filter(username__iexact=u_name):
            if(i.username==u_name):
                flag2=True
        if flag:
            print('Email taken already.')
            messages.info(request, 'Email taken already.')
            form = register_restaurant_form()

        elif flag2:
            print('User Name Aready Taken')
            messages(request, 'User Name Aready Taken')
            form = register_restaurant_form()

        elif form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
            print('Password did not match.')
            messages(request, 'Password did not match.')
            form = register_restaurant_form()

        else:
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.contact_no = form.cleaned_data.get('contact_no')
            user.profile.is_customer = True
            user.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('index')
    else:
        form = register_restaurant_form()
    return render(request, 'users/restaurant_registration.html', {'form': form})


def login_user_view(request):
    if request.method == 'POST':
        print('LOGIN')
        user_name = request.POST.get('username')
        print(user_name)
        pass_word = request.POST.get('password')
        print(pass_word)
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('/')
    else:
        return render(request, 'users/login.html')



def logout_view(request):
    auth.logout(request)
    return redirect('index')