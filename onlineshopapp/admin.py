from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'image', 'id')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'id')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)