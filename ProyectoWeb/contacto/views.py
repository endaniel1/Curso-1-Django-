from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import EmailMessage #Para manipulacion de envio de Email

# Create your views here.

def contact(request):
	formContact = ContactForm()
	if request.method == "POST":
		formContact = ContactForm(data=request.POST)

		if formContact.is_valid():
			nombre = request.POST.get("name")
			email = request.POST.get("email")
			content = request.POST.get("content")

			email = EmailMessage(
				"Mensaje desde la aplicacion django", #Encabezado a mostrar
				 #Descripcion del email
				"El Usuario con nombre {} con la Direcciòn {} escribe lo siguiente:\n\n {}".format(nombre, email, content),
				"", #Email de quien viene
				["endaniel1997@gmail.com"], #Coloco a quien va a recivir este email
				reply_to = [email]
			)

			# Aqui chequeo si ay un error
			try:
				email.send()
				return redirect("/contact/?valido")
			except Exception as e:
				# si da un error mandamos una varible
				return redirect("/contact/?no_valido")

	return render(request, "contact/contact.html", {
		"form":formContact
	})
