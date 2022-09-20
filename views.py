from http.client import HTTPResponse
from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Ciudad, Persona, Tipo_documento
from .forms import PersonaForm

# Create your views here.
def index(request):
    usuarios =  Persona.objects.all()
    template = loader.get_template('usuarios/index.html')
    context={'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))  

def delete_usuario(request, usuario_id):
    usuario = Persona.objects.get(id = usuario_id)
    usuario.delete()
    return redirect('/usuarios/')

def ciudades (request):
    new_ciudad = Ciudad.objects.all()
    template = loader.get_template('usuarios/ciudad.html')
    context = {'new_ciudad': new_ciudad,}
    return HttpResponse(template.render(context, request))

def nueva_ciudad(request):
    nuevo_nombre = request.POST["nombreC"]
    nueva_descripcion = request.POST["descripcionC"]
    city = Ciudad(nombre=nuevo_nombre, descripcion=nueva_descripcion)
    city.save()
    return redirect('/usuarios/ciudad/')
   
def delete_ciudad(request, ciudad_id):
    city = Ciudad.objects.get(id = ciudad_id)
    city.delete()
    return redirect('/usuarios/ciudad/')

def documento (request):
    documento = Tipo_documento.objects.all()
    template = loader.get_template('usuarios/documento.html')
    context = {'documentos': documento,}
    return HttpResponse(template.render(context, request))

def nuevo_documento(request):
    nuevo_nombre = request.POST["nombreTD"]
    nueva_descripcion = request.POST["descripcionTD"]
    dc = Tipo_documento(nombre=nuevo_nombre, descripcion=nueva_descripcion)
    dc.save()
    return redirect('/usuarios/documentos/')
   
def delete_documento(request, documento_id):
    dc = Tipo_documento.objects.get(id = documento_id)
    dc.delete()
    return redirect('/usuarios/documentos/')

def nueva_persona(request):
    if request.method == 'POST': 
        form = PersonaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombres']
            apellido = form.cleaned_data['apellidos']
            tipodocumento = form.cleaned_data['id_tipo_documento']
            documento = form.cleaned_data['documento']
            lugarresidencia = form.cleaned_data['lugar_de_residencia']
            fechanacimiento = form.cleaned_data['fecha_nacimiento']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['password']
            persona = Persona(nombres=nombre, apellidos=apellido, id_tipo_documento=tipodocumento, documento=documento, 
            lugar_de_residencia=lugarresidencia, fecha_nacimiento=fechanacimiento, correo=correo, telefono=telefono, usuario=usuario,
            password=contrasena)
            persona.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PersonaForm()
    return render(request, 'usuarios/crear_usuario.html', {'form':form})