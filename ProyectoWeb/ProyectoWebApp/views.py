from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
	
	return render(request, "ProyectoWebApp/home.html")


def shop(request):
	
	return render(request, "ProyectoWebApp/shop.html") 
