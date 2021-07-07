from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('user', user, name='user'),
]