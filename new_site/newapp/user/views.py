
from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from newapp.forms import LoginForm, RegisterForm
from newapp.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.

def login_user(request):
    print("Something")
    form = AuthenticationForm()
    if request.method == "POST":       
        form = AuthenticationForm(request ,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("Username:", username)
            print("Password:", password)
            print("Request:", request)
            # user = User.objects.filter(username=form.cleaned_data['username']).first()
            user = authenticate(request, username=username, password=password)
            print("User:", user)
            # print(user, form.cleaned_data['username'], form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('login_user')
        else:
            return redirect('index')
    return render(request, 'login.html', {'form':form})




def register(request):
    form = RegisterForm(request.POST)
    
    if form.is_valid():
        chack_user = User.objects.filter(email=form.cleaned_data['email']).first()
        if not chack_user:
            user = User(name=form.cleaned_data['name'],
                        surname=form.cleaned_data['surname'],
                        email=form.cleaned_data['email'],
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password'],
                        admin=form.cleaned_data['admin'],
                        )
            user.save()
            
            return redirect('login_user')
        else:
            messages.warning(request, 'Email is already taken.')
            return redirect('register')
    return render(request, 'register.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    user_id = None
    
    return render(request, 'profile.html', {'user_id':user_id})
