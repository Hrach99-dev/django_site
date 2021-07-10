from django.contrib.auth import hashers
from .forms import AddProduct
from django.shortcuts import render, redirect
from .models import Product


from django.contrib import messages

from django.contrib import auth

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password, make_password



# Create your views here.




def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users':users})


def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        username = User.objects.filter(email=email).first().username

        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
    

    return render(request, 'login.html', {})



def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        is_saler = request.POST.get('is_saler', False)
        
        if is_saler == 'on':
            is_saler = True

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is Taken')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is Taken')
            else:
                passowrd_hash = make_password(password1, hasher='pbkdf2_sha256')
            
                user = User(first_name=first_name, last_name=last_name,
                            username=username, email=email,
                            password=passowrd_hash, is_staff=is_saler)
                user.save()
                messages.success(request, 'Thanks for the registration!')
                return redirect('login')
        else:
            messages.warning(request, 'Password not matching...')

    return render(request, 'register.html', {})





def logout(request):
    auth.logout(request)
    return redirect('login')





# @login_required
def profile(request):
    user_id = request.user
    
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
