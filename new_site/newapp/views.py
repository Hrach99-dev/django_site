
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, AddProduct
from .models import User
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import messages
# Create your views here.


# session = SessionStore()


def index(request):
    users = User.objects.all()

    return render(request, 'index.html', {'users':users})



def login(request):
    form = LoginForm(request.POST)
    
    if form.is_valid():
        user = User.objects.filter(email=form.cleaned_data['email']).first()
        if user:
           
            # session['user_id'] = user.id
            return redirect('profile')
        else:
            return redirect('register')

    return render(request, 'login.html', {'form':form})




def register(request):
    form = RegisterForm(request.POST)
    
    if form.is_valid():
        chack_user = User.objects.filter(email=form.cleaned_data['email']).first()
        if not chack_user:
            user = User(email=form.cleaned_data['email'],
                        name=form.cleaned_data['name'],
                        surname=form.cleaned_data['surname'],
                        password=form.cleaned_data['password'],
                        admin=form.cleaned_data['admin'],
                        )
            user.save()
            
            return redirect('login')
        else:
            messages.warning(request, 'Email is already taken.')
            return redirect('register')
    return render(request, 'register.html', {'form':form})



def profile(request):
    # a = session['user_id']
    return render(request, 'profile.html')
