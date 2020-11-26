from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def contact(request):
	formContact = ContactForm()
	return render(request, "contact/contact.html", {
		"form":formContact
	})
