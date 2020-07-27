from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
	return render(request,"busqueda_productos.html")

def buscar(request):
	#Aqui vemos si viene la varible prd por get
	if request.GET["prd"]:
		#message = "Articulo buscado: %r" %(request.GET["prd"])
		producto = request.GET["prd"]
		#Comprobamos si su longitud no es mayor a 20
		if len(producto)>20:
			message="Texto de busqueda muy largo"
		else:
			#Para buscar o hacer un filtro senciilamente mandamos a llamar a la clase
			#despues con el metodo object.filter le indicamos por q campo vamos a buscar
			#y __icontains le indicamos por q valor va a buscar __icontains sirve como una condicinal Like
			articulos = Articulos.objects.filter(mombre__icontains=producto)
			return render(request,"resultados_busqueda.html",{
				"articulos":articulos, "query":producto
			})#retornamos aqui a la vista
	else:
		#sino viene nada le mandamos un mensaje
		message = "No haz Introduccido Nada"
	return HttpResponse(message)#retornamos aqui a la vista sino viene nada

def contacto(request):
	if request.method == "POST":
		"""
		#Para Capturar los datos del formulario de forma manual
		subject=request.POST['asunto']#Asunto del mensaje
		#mensaje 
		message=request.POST['mensaje']+" "+ request.POST["email"]
		email_form=settings.EMAIL_HOST_USER #destino al q va
		
		recipient_list=["endaniel1997@gmail.com"]#lista de quien lo va arecivir

		#Aqui recive la clase send_mail()
		#el asunto del mensaje
		#el mensaje
		#email de destion
		#y qui va recivirlo
		send_mail(subject,
			message,
			email_form,
			recipient_list)

		return render(request,"contacto.html")
		"""

		miFormulario=FormularioContacto(request.POST)
		if miFormulario.is_valid():
			infForm=miFormulario.cleaned_data
			send_mail(infForm["asunto"],
				infForm["mensaje"],
				infForm.get("email",""),
				["endaniel1997@gmail.com"],)

			return render(request,"gracias.html")
	else:
		miFormulario=FormularioContacto()

	return render(request,"formulario_contacto.html",
		{"form":miFormulario})