from django.urls import path

from ProyectoWebApp import views #vistas de nuestra app
from django.conf import settings #configuraciones de nuestro proyecto
from django.conf.urls.static import static #para las url estaticas

urlpatterns = [
    path('', views.home, name="Home"),
    path('shop', views.shop, name="Shop")
]
#Aqui registramo q este concadenado la rutas de nuestras imagenes
"""
la clase static()  se le pasa como parametro la url de MEDIA y
segundo parametro q la raiz del documento la configuracion de la ruta de MEDIA
"""
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)