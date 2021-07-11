from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    price = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    published = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Buyer(models.Model):
    user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    product_obj  = models.ForeignKey(Product, on_delete=models.CASCADE)
