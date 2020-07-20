from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render

"""Clase Persona"""
class Persona(object):

	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido


#HttpResponse Siempre se importa esta clase, esto para el manejo de vista
#las funciones funciones  se manejan como vista
def saludo(request): #Primera vista
	#para retornar algo sencillo siempre se llama a la clase 
	#HttpResponse() pasandolo un argumento 
 
	#clases y variables a usar para la plantilla
	p1 = Persona("Enrique","Rodriguez")
	#nombre="Enrique"
	#apellido="Rodriguez"
	fecha_ahora = datetime.datetime.now()
	temas_curso = ["Plantillas","Filtros","Vista","Cargadores","Condicionales"]

	#CaRGO AQUI DE FORMA MANUAL EL ARCHIVO CON EL METODO open()
	#document_externo = open("C:/Users/ENRIQUE/Documents/Enrique/Python/Django/mysite/mysite/template/miplantilla.html")

	#plt = Template(document_externo.read())# se lee el archivo o documento

	#document_externo.close()# Se sierra el documento o archivo

	#document_externo=loader.get_template("miplantilla.html")
	"""
	ctx = Context({
		"fecha":fecha_ahora,
		"nombre_persona":p1.nombre,
		"apellido_persona":p1.apellido,
		"temas":temas_curso
	})# se crea una instancia del contenido
	
	document = document_externo.render({
		"fecha":fecha_ahora,
		"nombre_persona":p1.nombre,
		"apellido_persona":p1.apellido,
		"temas":temas_curso
	})#y aqui se renderiza nuestro documento
	"""

	#Aqui renderizamos la vista con el metodo render()
	#Se le pasa por parametro el request, el nombre del archivo y despues un diccionario de datos
	return render(request, "miplantilla.html", {
		"fecha":fecha_ahora,
		"nombre_persona":p1.nombre,
		"apellido_persona":p1.apellido,
		"temas":temas_curso
	})



def despedida(request):#segunda vista
	
	return HttpResponse("Hasta luego desde Django")



def damefecha(request):

	fecha_actual=datetime.datetime.now()

	document="""
	<html>
		<body>
			<h2>fecha y hora actual %s</h2>
		</body>
	</html>""" % fecha_actual

	return HttpResponse(document)

def calculedad(request,edad,ano):
	
	periodo = ano - 2020
	edadFutura = edad + periodo
	document = """
	<html>
		<body>
			<h2>En EL Año %s Tendras %s Años</h2>
		</body>
	</html>""" %(ano,edadFutura)

	return HttpResponse(document)

def curso(request):
	
	fecha_actual=datetime.datetime.now()

	return render(request,"curso.html",{
		"damefecha":fecha_actual
	})