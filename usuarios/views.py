import http
from http.client import HTTPResponse
from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from mvcCRUD.usuarios.models import persona

# Create your views here.
def index(request):
    usuarios =  persona.objects.all()
    template = loader.get_template('usuarios/index.html')
    context={
        'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))  