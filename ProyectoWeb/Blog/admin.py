from django.contrib import admin
from .models import Category, Post

# Register your models here.

"""docstring for CategoryAdmin"""
class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ("created","updated")

"""docstring for PostAdmin"""
class PostAdmin(admin.ModelAdmin):
	readonly_fields = ("created","updated")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
