from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('login',  login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout'),
    path('addprod', addprod, name='addprod'),
    
]