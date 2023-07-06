from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", index, name="index"),    
    path("sobrenosotros/", sobrenosotros, name="sobrenosotros"),    
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path("catalogo/", catalogo, name="catalogo"),
    path("logout/", logout, name="logout"),
    path("registro/", registro, name="registro"),
    path("historial/", historial, name="historial"),
    path("addtocart/<codigo>", addtocart, name="addtocart"),
    path("sumcarro/<codigo>", sumcarro, name="sumcarro"),
    path("dropitem/<codigo>", dropitem, name="dropitem"),
    path("dropstack/<codigo>", dropstack, name="dropstack"),
    path("limpiar/", limpiar, name="limpiar"),
    path("carrito/", carrito, name="carrito"),
    path("comprar/", comprar, name="comprar"),
    path("suscribir/", suscribir, name="suscribir"),
    path('eliminar_usuario/<str:username>/', eliminar_usuario, name='eliminar_usuario'),
]

