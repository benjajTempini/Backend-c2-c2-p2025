from django.http import HttpResponse
from django.shortcuts import render
from . import models

def inicio(request):
    return HttpResponse("Hola mundo desde django")

def mostrar_bienvenida(request):
    tu_nombre = "Benjamin Rojas"
    return HttpResponse(f"Bienvenidos a mi app Django, {tu_nombre}!")

def home(request):
    return HttpResponse("Quetu ace aca?? vete a jugar ROCKET LEAGUE!!!!" \
    "" "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "\
    "Aca tienes las demas rutas" \
    "/inicio/" \
    "/mostrar_bienvenida/" \
    "ez")

def lista_producto(request):
    productos = models.Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos':productos})