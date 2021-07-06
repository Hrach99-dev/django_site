from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    timestamp = models.DateField(auto_now=True)
    published = models.BooleanField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Buyer(models.Model):
    user = models.ForeignKey("newapp.CustomUser", on_delete=models.CASCADE)
   #product_id = models.ForeignKey(Product(id), on_delete=models.CASCADE)