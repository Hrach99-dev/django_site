from django.contrib import admin
from .models import CustomUser, Product, Buyer
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Buyer)