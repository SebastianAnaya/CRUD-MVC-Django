from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ciudad/', views.ciudades, name='ciudades'),
    path('delete_usuario/<int:usuario_id>/', views.delete_usuario, name='delete_usuario'),
    path('crear_ciudad/', views.nueva_ciudad, name='crear_ciudad'),
    path('delete_ciudad/<int:ciudad_id>/', views.delete_ciudad, name='delete_ciudad'),
    path('documentos/', views.documento, name='documento'),
    path('crear_documento/', views.nuevo_documento, name='crear_documento'),
    path('delete_documento/<int:documento_id>/', views.delete_documento, name='delete_documento'),
    path('crear_persona/', views.nueva_persona, name='crear_persona')
]
