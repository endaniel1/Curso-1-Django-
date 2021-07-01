from django.shortcuts import render
from .models import Products, CategoryProd

# Create your views here.

def shop(request):
	products = Products.objects.all()

	return render(request, "shop/shop.html", {
		"products": products
	}) 