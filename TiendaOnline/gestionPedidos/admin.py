from django.contrib import admin

from gestionPedidos.models import Clientes,Articulos,Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
	list_display=("nombre","direccion","tlno")
	search_fields=("nombre","tlno")

class ArtitulosAdmin(admin.ModelAdmin):
	"""docstring for AritulosAdmin"""
	list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
	"""docstring for PedidosAdmin"""
	list_display=("numero","fecha")
	list_filter=("fecha",)
	date_hierarchy="fecha"
	
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArtitulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)