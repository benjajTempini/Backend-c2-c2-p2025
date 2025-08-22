from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('mostrar_bienvenida/', views.mostrar_bienvenida),
    path('', views.home),
]
