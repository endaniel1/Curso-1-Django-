from django.contrib import admin

from gestionPedidos.models import Clientes,Articulos,Pedidos

# Register your models here.

"""Clase a utilizar ClientesAdmin"""
class ClientesAdmin(admin.ModelAdmin):
	list_display=("nombre","direccion","tlno")
	#Aqui con la variable list_filter la igualamos a una tupla
	#Con esto le indicamos cuales van a hacer los campos para la busqueda a realizar
	search_fields=("nombre","tlno")

"""Clase a utilizar AritulosAdmin"""
class ArtitulosAdmin(admin.ModelAdmin):	
	list_filter=("seccion",)

"""Clase a utilizar PedidosAdmin"""
class PedidosAdmin(admin.ModelAdmin):
	#Aqui con la variable list_display lo igualamos a una tupla
	#Le decimos a nuestro panel q muestre esto campos
	list_display=("numero","fecha")
	#Aqui con la variable list_filter lo igualamos a una tupla
	#Y le indicamos cual va a ser la el filtro para buscar
	list_filter=("fecha",)
	#Aqui le indicamos el datos q va a heredar para q busque
	date_hierarchy="fecha"
	
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArtitulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)