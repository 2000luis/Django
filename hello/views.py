from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # aqui renderizas un html template que gardamos en la carpeta templates pero puede ser el nombre que quieras
    
    # la pagina renderiza el html con solo su ubicaion dentro nuestra carpeta maestra qque es hello
    
    return render(request, "subCarpeta/index.html")

def otraPagina(request):
    return HttpResponse("hola esta es otra pagina")

def saludo(request, Usario):
    return render(request, "subCarpeta/greet.html", {
      #dentro del dictionario el nombre que pongas en el string va hacer como variable para que lo puedas usar en el html
      "Usarios11": Usario.capitalize()  
    })
    