from django.urls import path
from . import views

#Esta variable te sirve para nombrar tu application y no se vayan a crusar urls nombres y se puede usar como nombre para localizar urls en un link en html
app_name = "añoNuevo"
urlpatterns = [
     path("", views.index, name="index")
]