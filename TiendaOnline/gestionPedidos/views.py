from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
	return render(request,"busqueda_productos.html")

def buscar(request):
	
	if request.GET["prd"]:
		#message = "Articulo buscado: %r" %(request.GET["prd"])
		producto = request.GET["prd"]
		if len(producto)>20:
			message="Texto de busqueda muy largo"
		else:
			articulos = Articulos.objects.filter(mombre__icontains=producto)
			return render(request,"resultados_busqueda.html",{
				"articulos":articulos, "query":producto
			})

	else:
		message = "No haz Introduccido Nada"

	return HttpResponse(message)

def contacto(request):
	if request.method == "POST":
		return render(request,"gracias.html")
	return render(request,"contacto.html")