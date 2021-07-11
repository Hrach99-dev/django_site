from django.urls import path
from .views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('login',  login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout'),
    path('addprod', addprod, name='addprod'),
    path('buy/<int:product_id>', buy_product, name='buy_product')
] 


