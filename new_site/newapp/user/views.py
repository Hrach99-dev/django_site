
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from newapp.forms import LoginForm, RegisterForm
from newapp.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.

def login_user(request):
    
    form = LoginForm(request.POST)
    if form.is_valid():

        # user = User.objects.filter(email=form.cleaned_data['username']).first()
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        print(user)
        if user is not None:
            # login(request, user)
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
