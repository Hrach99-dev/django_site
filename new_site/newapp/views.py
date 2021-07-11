from .forms import AddProduct
from django.shortcuts import render, redirect
from .models import Buyer, Product

from django.contrib import messages

from django.contrib import auth

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import make_password



# Create your views here.




def index(request):
    products = Product.objects.filter(published=True).all()
    return render(request, 'index.html', {'products':products})


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


@login_required
def addprod(request):
    form = AddProduct(request.POST, request.FILES)
    if form.is_valid():
        if request.user.is_staff == True:
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            price=form.cleaned_data['price']
            published=request.POST.get('published', False)
            author = request.user
            image = form.cleaned_data['image']

            if published == 'on':
                published = True
            else:
                published = False

            if len(price) - 1 != '$':
                price = price + '$'
            else:
                price = price
            

            prod = Product(
                title = title,
                description = description,
                image = image,
                price = price,
                published = published,
                author = author,
            )
            prod.save()

            return redirect('index')

    return render(request, 'addprod.html', {'form':form})




@login_required
def profile(request):
    
    user = request.user
    

    if user.is_staff:
        all_item = Product.objects.filter(author=user).all()
    else:
        all_item = Buyer.objects.filter(user_obj=user).all()
    return render(request, 'profile.html', {'all_item':all_item})





@login_required
def buy_product(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
 
    buyer = Buyer(user_obj=user, product_obj=product)
    buyer.save()
    
    
    return redirect('profile')


def update_product(request, product_id):
    
    product = Product.objects.get(id=product_id)

    form = AddProduct(request.POST, request.FILES)

    if form.is_valid():
        product.title=form.cleaned_data['title']
        product.description=form.cleaned_data['description']
        price = form.cleaned_data['price']

        if len(price) - 1 != '$':
            price = price + '$'
        else:
            price = price

        product.price=price

        published=request.POST.get('published', False)

        if published == 'on':
            published = True
        product.published = published

        product.author = request.user

        product.image = form.cleaned_data['image']

        product.save()
        return redirect('index')
    elif request.method == 'GET':
        form.cleaned_data['title'] = product.title
        form.cleaned_data['description'] = product.description
        form.cleaned_data['price'] = product.price
        if product.published == True:
            form.cleaned_data['published'] = 'on'
        else:
            form.cleaned_data['published'] = 'off'
        form.cleaned_data['image'] = product.image

    return render(request ,'addprod.html', {'form':form})




@login_required
def delete_product(request ,product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('index')
