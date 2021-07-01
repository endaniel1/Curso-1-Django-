from django.contrib import admin
from .models import CategoryProd, Products

# Register your models here.

"""docstring for CategoryProdAdmin"""
class CategoryProdAdmin(admin.ModelAdmin):
	readonly_fields = ("created","updated")

"""docstring for ProductsAdmin"""
class ProductsAdmin(admin.ModelAdmin):
	readonly_fields = ("created","updated")

admin.site.register(CategoryProd, CategoryProdAdmin)
admin.site.register(Products, ProductsAdmin)
