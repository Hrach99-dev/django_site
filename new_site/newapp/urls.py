from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login',  login_request, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout_view', logout_view, {'redirect_authenticated_user': True}, name='logout_view'),
    path('addprod', addprod, name='addprod'),
    
]