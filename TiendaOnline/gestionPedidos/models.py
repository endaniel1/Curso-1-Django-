from django.db import models

# Create your models here.

#Las Clase son los modelos q se van a crear para las tablas

"""Clase de Clientes"""
class Clientes(models.Model):
	nombre=models.CharField(max_length=30)
	direccion=models.CharField(max_length=50)
	email=models.EmailField(blank=True,null=True)
	tlno=models.CharField(max_length=7)

"""Clase de Articulos"""
class Articulos(models.Model):
	mombre=models.CharField(max_length=30)
	seccion=models.CharField(max_length=20)
	precio=models.IntegerField()

	def __str__(self):
		return "El Nombre Es: %s La Seccion Es: %s Y El Precio Es %s " % (self.mombre,self.seccion,self.precio)

"""Clase de Pedidos"""
class Pedidos(models.Model):
	numero=models.IntegerField()
	fecha=models.DateField()
	entregado=models.BooleanField()
		
		

