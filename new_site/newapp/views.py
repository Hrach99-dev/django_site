from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, AddProduct


# Create your views here.




def index(request):
    return render(request, 'index.html')



def login(request):
    form = LoginForm(request.POST)
    
    if form.is_valid():
        return redirect('user')

    return render(request, 'login.html', {'form':form})




def register(request):
    form = RegisterForm(request.POST)
    
    if form.is_valid():
        return redirect('login')
    return render(request, 'register.html', {'form':form})



def user(request):
    return render(request, 'user.html')
