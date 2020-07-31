from django.contrib import admin
from .models import Service

# Register your models here.

"""Clase de ServiceAdmin"""
class ServiceAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated",) #Para q los datos e muestren de solo texto

#Registramos aqui para q muestre el modelo en el panel de administracion de django
admin.site.register(Service, ServiceAdmin) 
