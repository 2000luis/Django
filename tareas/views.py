from django.shortcuts import render

#Se agrego una lista de elementos llamada tareasIn que se ultilizara por dentro del codigo
tareasIn = ["luis","jaque","juan"]
# Create your views here.

#Despues se crean una funcion de tiene como nombre index, esta funcion renderizara el html de index el cual dara la estructura de esa pagina y despues se pasa un dicionario como argumento con un elemento con nombre tareaOut el cual se podra utilizar a dentro de html y se le pasa la lista del inicio tareaIn
def index(request):
    return render(request, "tareas/index.html", {
        "tareasOut": tareasIn
    })