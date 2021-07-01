from django.urls import path

from . import views #vistas de nuestra app

urlpatterns = [
    path('', views.shop, name="Shop")
]