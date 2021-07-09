from .forms import AddProduct
from django.shortcuts import render, redirect
from .models import User, Product


# Create your views here.




def index(request):
    users = User.objects.all()

    return render(request, 'index.html', {'users':users})



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
