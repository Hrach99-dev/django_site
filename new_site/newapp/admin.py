from django.contrib import admin

# Register your models here.
from .models import *



# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'name', 'surname', 'password',
#     'admin')
#     list_filter = ('email', 'admin')
#     search_fields = ('name', 'surname')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'timestamp',
    'published')
    list_filter = ['title', 'price', 'published']
    search_fields = ['title']
    ordering = ['price']


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id')
    list_filter = ['product_id']
    search_fields = ['user_id']