from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a email'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a password'}))
    
    

"""class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a name'}))
    surname = forms.CharField(label='Surname', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a surname'}))
    email = forms.CharField(label='Email', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a email'}))
    username = forms.CharField(label='Usrname', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a username'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a password'}))
    admin = forms.BooleanField(label='Admin', required=False)"""



class AddProduct(forms.Form):
    title = forms.CharField(label='Product name', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a product name'}))
    description = forms.CharField(label='Product description', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a product description'}))
    price = forms.CharField(label='Product price', required=True, widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'Enter a product price'}))
    # image = forms.ImageField(label='Product image', widget=forms.TextInput(attrs={'class':'w-50 mt-3 border pt-2 pb-2 border-primary', 'placeholder':'image'}))
    published = forms.BooleanField(label='Published', required=True)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user