from django import forms

"""docstring for ContactForm"""
class ContactForm(forms.Form):

	name = forms.CharField(label='Nombre', required=True, max_length="150")
	email = forms.EmailField(label='Correo', required=True)
	content = forms.CharField(label='Contenido', widget=forms.Textarea)
	
