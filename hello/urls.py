from django.urls import path
from . import views

urlpatterns = [
    # (como primer element dentro de path va un string con el cual quieras que sea la extension de el link, despues va que es lo que se va ver in la pagina y eso se importa desde el archivo de views por eso el views. el nombre de la funcion en archivo de views, despues va el nombre de la pagina que no sera visible)
    
    path("", views.index,name="index"),
    
    # Si se llegara a repetir algunos nombres de se cargara la pagina que vaya primero en esta lista
    
    path("luis", views.otraPagina, name="otra"),
    path("<str:Usario>", views.saludo, name="saludo"),
]