"""PrimerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin


#Se debe de anexar el include porque estas usando esa funcion dentro de path

#En este caso solo se anexo en import include, path
from django.urls import include, path

urlpatterns = [
    
    #Dentro de path como primer argumento se ingresa un string que es la extencion de esa app en el link principal de la pagina
    
    path('admin/', admin.site.urls),
    path('nombreDeExtencion/', include("hello.urls")),
    path('OtraEctencion/', include("AñoNuevo.urls")),
    #El include es para anexar el archivo de urls de la app tareas se pone la direccion de esa archivo
    path('tareas/', include("tareas.urls"))
]
