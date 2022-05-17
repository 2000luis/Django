
#Para poder agregar froms con django, este msimo tiene su porpia manera de hacer forms y asi se importan
from django import forms

# esta funcion se ocupa para llamar a reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

#para poder usar la funcion reverse que reversea el name de un path de urlpatterns
from django.urls import reverse

#Se agrego una lista de elementos llamada tareasIn que se ultilizara por dentro del codigo
#tareasInOutIndex = [ ]
# Create your views here.

#para poder crear forms con django se necesita crear una class con nombre cualquiera que se la pasa como argumento de django para crear forms y guardar inforacion
class NewTarea(forms.Form):
    #Aqui se crear el form con nombre cualquiera, se espesifica de que va hacer
    formadd = forms.CharField(label=("Nueva tarea"))
    
    #esta variable prioridad con tiene otro form que solo puede recibir valores numericos del 1 al 10 
    ###prioridad = forms.IntegerField(label= "prioridad", min_value=1, max_value=12)

#Despues se crean una funcion de tiene como nombre index, esta funcion renderizara el html de index el cual dara la estructura de esa pagina y despues se pasa un dicionario como argumento con un elemento con nombre tareaOut el cual se podra utilizar a dentro de html y se le pasa la lista del inicio tareaIn
def index(request):
    
    #este if chequa si no hay una variable llamada tareaIn en la peticion de esa sesion
    if "tareaInFIndex" not in request.session:
        
        #Si no esxiste esta variable pues se crea una aqui que es una lista vacia en esta ocacion
        request.session["tareaInFIndex"] = []
        
    return render(request, "tareas/index.html", {
        #Este codigo comentado se ocupa cuando la variable esta escrita afuera
        ###"tareasOut": tareasInOutIndex
        
        # ASi se escribe cuando esta internamente de la funcion por cada session abierta
        "tareasOut": request.session["tareaInFIndex"]
    })
    
#Esta funcion servira para agregar elementos a una lista del html index pero en otro html llamado agregar
def agregar(request):
    
    #Cuando se llama a esta funcion se verifica si request.method es igual a "POST" un protocol que espesifica un tipo de accion que se ejecuto en la app que significa que se esta insertando informacion
    if request.method == "POST":
        
        #La variable formulario guarda la creacion de una nueva tarea con informacion que se esta pasando desde la app que esta guardada en request.POST
        #La class NewTarea() la recoje porque es informacion esa class sabe interpretars
        formulario = NewTarea(request.POST)
        
        #En este if se valid la informacion que se esta pasando desde la app
        if formulario.is_valid():
            
            #Si la informacion esta verificada se limpiara y se almacena en .cleaned-data se podra obtener con la variable de el form por el cual fue ingresada
            #todo esto se guardara en una variable addtarea que ya tendra la informacion lista para usar 
            addtarea = formulario.cleaned_data["formadd"]
            
            #Aqui se pasa la informacion a la lista de tareasInOutIndex
            #tareasInOutIndex.append(addtarea)
            
            #OR  Aqui se pasa la informacion a una lista nueva por cada session abierta 
            request.session["tareaInFIndex"] = request.session["tareaInFIndex"] + [addtarea]
            #OR request.session["tareaInFIndex"] += [addtarea]
            
            
            return HttpResponseRedirect(reverse("ta:index"))
            
        #Si se aplica el else se le regresara su informacion con los detalles que fallaron con el formulario y esto lo hace el servidor 
        else:
            return render(request, "tareas/agregar.html",{ "formm": formulario 
        })
        
         
    return render(request, "tareas/agregar.html",{
        
        #Este se utiliza para crear una variable que se pueda usar dentro de html con informacion interna como esta la class NewTarea() con forms adentro
        "formm": NewTarea()
    })