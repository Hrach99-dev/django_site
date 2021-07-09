from django.urls import path
from .views import *
from .user.views import *


urlpatterns = [
    path('', index, name='index'),
    path('login_user', login_user, name='login_user'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout_view', logout_view, name='logout_view'),
    path('addprod', addprod, name='addprod')
]