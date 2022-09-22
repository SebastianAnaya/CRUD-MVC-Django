from cProfile import label
from dataclasses import field
from enum import auto
from msilib.schema import Class
from random import choices
from django import forms
from .models import Persona, Tipo_documento, Ciudad
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password

class TimesheetItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PersonaForm(forms.ModelForm):
    
    password2 =  forms.CharField(label = "Confirmar contraseña", widget= forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password2',
            'required': 'required',
        }
    ))
    
    class Meta: 
        model = Persona
        fields = '__all__'
        labels = {
            'nombres': 'Nombre', 
            'apellidos': 'Apellido', 
            'id_tipo_documento': 'Tipo de documento', 
            'documento': 'Documento', 
            'lugar_de_residencia': 'Lugar de residencia', 
            'fecha_nacimiento': 'Fecha de nacimiento', 
            'correo': 'Correo electrónico', 
            'telefono': 'Teléfono', 
            'usuario': 'Usuario', 
            'password': 'Contraseña',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}), 
            'apellidos': forms.TextInput(attrs={'class':'form-control'}), 
            'id_tipo_documento': forms.Select(attrs={'class':'form-control'}), 
            'documento': forms.TextInput(attrs={'class':'form-control'}),
            'lugar_de_residencia': forms.Select(attrs={'class':'form-control'}), 
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 
                    'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                    }), 
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'id': 'password1',})
        }
    
    def clean_password2(self): 
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        persona = super().save(commit=False)
        persona.password = ('password')
        if commit:
            persona.save()
        return persona
