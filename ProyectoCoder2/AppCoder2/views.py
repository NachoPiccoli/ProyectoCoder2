from django.shortcuts import render
#from django.http import HttpResponse # ya no lo uso más

from django.shortcuts import render
from AppCoder2.models import Estudiante

# Create your views here.

def mostrar_inicio (request):

    estudiante=Estudiante(nombre="Juan", apellido="Perez", email="ajs@hotmail.com")
    contexto= {"estudiante_1":estudiante}

    return render(request, "AppCoder2/inicio.html",contexto)
    
    #return HttpResponse ("Hola Mundo ProyectoPython2")