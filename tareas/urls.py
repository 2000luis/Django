#Se debe agregar esta libreria de django.urls para importar path
from typing import Pattern
from django.urls import path
from django.urls.resolvers import URLPattern

#Luego para acceder desde la misma carpeta se ustiliza el punto: . , despues se importa los views
from . import views

#Se crean una lista para almacenar los paths 
urlpatterns = [
    #En la funcion path recibe como primer argumento un string que recibira al final de la extension que impemento en el urls.py de la carpeta del proyecto 
    #En este caso despues de tareas/ y ira vacio porque es la pagina index osea principal
    path("", views.index.py, name = "index")
]