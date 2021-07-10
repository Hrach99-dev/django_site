
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a username'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a password'}))
        
    class Meta:
        model = User
        fields = ('username', 'password' )


class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a name'}))
    surname = forms.CharField(label='Surname', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a surname'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a email'}))
    username = forms.CharField(label='Usrname', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a username'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a password'}))
    admin = forms.BooleanField(label='Admin', required=False)


class AddProduct(forms.Form):
    title = forms.CharField(label='Product name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a product name'}))
    description = forms.CharField(label='Product description', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a product description'}))
    price = forms.CharField(label='Product price', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a product price'}))
    # image = forms.ImageField(label='Product image', widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'image'}))
    published = forms.BooleanField(label='Published', required=True)