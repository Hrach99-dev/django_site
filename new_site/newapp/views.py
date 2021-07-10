from django.contrib.auth import login, authenticate
from .forms import AddProduct, NewUserForm
from django.shortcuts import render, redirect
from .models import User, Product


from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.contrib import auth

from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password

# Create your views here.

from django.views.generic import FormView, View



def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users':users})






def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form":form})


'''def login_view(request):
    
    form = LoginForm(request.POST)
    if form.is_valid():
        
        username = User.objects.get(email=form.cleaned_data['email']).username
        password = request.POST['password']

        print(username, password)

        check_user = User.objects.get(username=username)

        if check_password(password, check_user.password):
            # user = authenticate(request, username=username, password=check_user.password)
            new_user = auth.authenticate(request, username=username, password=password)
            
            # print(check_password('gadot', check_user.password))  <<<<<<<<< TRUE
            print(new_user)

            if new_user is not None:
                
                auth.login(request, new_user)

    
    return render(request, 'login.html', {'form':form})'''





def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, "register.html", {"register_form":form})



'''def register(request):
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
            
            return redirect('login_view')
        else:
            messages.warning(request, 'Email is already taken.')
            return redirect('register')
    return render(request, 'register.html', {'form':form})'''





def logout_view(request):
    auth.logout(request)
    return redirect('login')





# @login_required
def profile(request):
    user_id = None
    
    return render(request, 'profile.html', {'user_id':user_id})





def addprod(request):
    form = AddProduct(request.POST)
    if form.is_valid():
        prod = Product(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            price=form.cleaned_data['price'],
            timestamp=form.cleaned_data['timestamp'],
            published=form.cleaned_data['published'],
            user=form.cleaned_data['user']
        )
        prod.save()

        return redirect('index')

    return render(request, 'addprod.html', {'form':form})
