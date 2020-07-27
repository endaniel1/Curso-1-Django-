from django import forms


"""docstring for FormularioContacto"""
class FormularioContacto(forms.Form):

	asunto = forms.CharField()
	email = forms.EmailField()
	mensaje = forms.CharField()
