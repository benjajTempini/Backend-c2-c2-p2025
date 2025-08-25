from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola mundo desde django")

def mostrar_bienvenida(request):
    tu_nombre = "Benjamin Rojas"
    return HttpResponse(f"Bienvenidos a mi app Django, {tu_nombre}!")

def home(request):
    return HttpResponse("Quetu ace aca?? vete a jugar ROCKET LEAGUE!!!!")