from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader
from .models import Familiares

def crear_familiar(request,nombre,apellido,fecha_nacimiento,edad,email):
    
    plantilla = loader.get_template('f_creado.html')
    
    familiar = Familiares(nombre=nombre, apellido=apellido, nacimiento=fecha_nacimiento, edad=edad, email=email)

    familiar.save()
    
    diccionario = {'familiares':familiar}
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
    

def listado_familiares(request):
    
    template = loader.get_template('principal_familiares.html')
    lista_familiares = Familiares.objects.all()
    render = template.render({'lista':lista_familiares})
    return HttpResponse(render)

def inicio(request):
    template = loader.get_template('inicio.html')
    render = template.render({})
    return HttpResponse(render)