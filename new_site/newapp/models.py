from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    admin = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f'User - {self.name} {self.surname}'
    
    def __str__(self) -> str:
        return self.name
    
    

class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    # image = models.ImageField(null=True, blank=True)
    price = models.CharField(max_length=64)
    timestamp = models.DateField(auto_now=True)
    published = models.BooleanField()
    user = models.ForeignKey(User(id), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Buyer(models.Model):
    user_id = models.ForeignKey(User(id), on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product(id), on_delete=models.CASCADE)
