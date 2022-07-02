
from django.urls import path
from .views import  crear_familiar, listado_familiares, inicio

urlpatterns = [

   # path('inicio', familiares)
    path('creacion/<nombre>/<apellido>/<fecha_nacimiento>/<edad>/<email>', crear_familiar),
    path('listado/', listado_familiares),
    path('', inicio )
]