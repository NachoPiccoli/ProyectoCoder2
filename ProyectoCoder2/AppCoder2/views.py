from django.shortcuts import render
#from django.http import HttpResponse # ya no lo uso más

from django.shortcuts import render

# Create your views here.

def mostrar_inicio (request):
    return render(request, "AppCoder2/inicio.html")
    
    #return HttpResponse ("Hola Mundo ProyectoPython2")