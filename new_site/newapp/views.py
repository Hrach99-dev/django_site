from django.shortcuts import render



# Create your views here.


# class-nerov mi ereq viewser@ ------------------<<<<<<

def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')