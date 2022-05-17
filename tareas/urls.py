#Se debe agregar esta libreria de django.urls para importar path
from typing import Pattern
from django.urls import path
from django.urls.resolvers import URLPattern

#Luego para acceder desde la misma carpeta se ustiliza el punto: . , despues se importa los views
from . import views

#Esta variable te sirve para nombrar tu application y no se vayan a crusar urls nombres y se puede usar como nombre para localizar urls en un link en html
app_name = "ta"

#Se crean una lista para almacenar los paths 
urlpatterns = [
    #En la funcion path recibe como primer argumento un string que recibira al final de la extension que impemento en el urls.py de la carpeta del proyecto 
    #En este caso despues de tareas/ y ira vacio porque es la pagina index osea principal
    path("", views.index, name = "index"),
    
    #En este path redigiremos a otra pagina con la extension agregar/ que obtendra las instruciones la funcion agregar que se encuentra en el archivo views
    path("agregar/", views.agregar, name = "agregar")
]