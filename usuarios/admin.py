from django.contrib import admin
from .models import Tipo_documento, Ciudad, Persona

admin.site.register(Tipo_documento)
admin.site.register(Ciudad)
admin.site.register(Persona)

# Register your models here.
