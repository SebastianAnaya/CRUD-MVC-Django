import http
from http.client import HTTPResponse
from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import ciudad, persona, tipo_documento

# Create your views here.
def index(request):
    usuarios =  persona.objects.all()
    template = loader.get_template('usuarios/index.html')
    context={
        'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))  

def delete_usuario(request, usuario_id):
    usuario = persona.objects.get(id = usuario_id)
    usuario.delete()
    return redirect('/usuarios/')

def ciudades (request):
    new_ciudad = ciudad.objects.all()
    template = loader.get_template('usuarios/ciudad.html')
    context = {'new_ciudad': new_ciudad,}
    return HttpResponse(template.render(context, request))

def nueva_ciudad(request):
    nuevo_nombre = request.POST["nombreC"]
    nueva_descripcion = request.POST["descripcionC"]
    city = ciudad(nombre=nuevo_nombre, descripcion=nueva_descripcion)
    city.save()
    return redirect('/usuarios/ciudad/')
   
def delete_ciudad(request, ciudad_id):
    city = ciudad.objects.get(id = ciudad_id)
    city.delete()
    return redirect('/usuarios/ciudad/')

def documento (request):
    documento = tipo_documento.objects.all()
    template = loader.get_template('usuarios/documento.html')
    context = {'documentos': documento,}
    return HttpResponse(template.render(context, request))

def nuevo_documento(request):
    nuevo_nombre = request.POST["nombreTD"]
    nueva_descripcion = request.POST["descripcionTD"]
    dc = tipo_documento(nombre=nuevo_nombre, descripcion=nueva_descripcion)
    dc.save()
    return redirect('/usuarios/documentos/')
   
def delete_documento(request, documento_id):
    dc = tipo_documento.objects.get(id = documento_id)
    dc.delete()
    return redirect('/usuarios/documentos/')