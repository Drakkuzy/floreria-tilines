from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
import requests
from datetime import datetime 
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from api.models import *

def historial(request):
    venta = Venta.objects.filter(cliente=request.user)
    return render(request, "core/historial.html", {'venta': venta})


def index(request):
    fecha = datetime.today().strftime('%d-%m-%Y')
    response = requests.get(f"https://mindicador.cl/api/dolar/{fecha}")
    dolar = float(response.json()["serie"][0]["valor"])
    plantas = Producto.objects.all()

    for planta in plantas:
        planta.endolares = round(planta.precio / dolar, 1)
    return render(request, 'core/index.html', {'plantas':plantas, 'carro':request.session.get("carro",[])})


def comprar(request):
    suscrito = UsuarioSuscrito.objects.all()
    
    if not request.user.is_authenticated:
        return redirect('login')

    carro = request.session.get('carro', [])
    total = 0

    for c in carro:
            total += c[5]

    venta = Venta(cliente=request.user, total=total)
    venta.save()

    for c in carro:
        producto = Producto.objects.get(codigo=c[0])
        cantidad = c[2]

        if cantidad <= producto.stock:
            producto.stock -= cantidad
            producto.save()

            detalle = Detalle(venta=venta, producto=producto, cantidad=cantidad, precio=c[1])
            detalle.save()

    request.session['carro'] = []
    return redirect('carrito')

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    new_carro = []
    for c in carro:
        if c[0] == codigo:
            if c[2] > 1:
                c[2] = c[2] - 1
                c[5] = c[5] - c[1]
                new_carro.append(c)
            else:
                pass
        else:
            new_carro.append(c)
    request.session["carro"] = new_carro
    return redirect(to="carrito")

def dropstack(request, codigo):
    carro = request.session.get("carro", [])
    new_carro = []
    for c in carro:
        if c[0] == codigo:
            if c[2] > 1:
                pass
        else:
            new_carro.append(c)
    request.session["carro"] = new_carro
    return redirect(to="carrito")

def addtocart(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for c in carro:
        if c[0] == codigo:
            c[2] = c[2] + 1
            c[5] = c[2] * c[1]
            break
    else:
        carro.append([codigo, producto.precio, 1, producto.imagen, producto.descripcion, producto.precio])
    request.session["carro"] = carro
    plantas = Producto.objects.all()
    return redirect(to="catalogo")

def sumcarro(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for c in carro:
        if c[0] == codigo:
            c[2] = c[2] + 1
            c[5] = c[2] * c[1]
            break
    else:
        carro.append([codigo, producto.precio, 1, producto.imagen, producto.descripcion, producto.precio])
    request.session["carro"] = carro
    plantas = Producto.objects.all()
    return redirect(to="carrito")

def carrito(request):
    plantas = Producto.objects.all()
    suscrito = Suscripcion.objects.filter(user=request.user)
    return render(request,'core/carrito.html', {'suscrito':suscrito,'plantas':plantas, 'carro':request.session.get("carro",[])})


def limpiar(request):
    request.session.flush()
    accesorios = Producto.objects.all()
    return render(request, 'core/index.html', {'accesorios':accesorios})

def sobrenosotros(request):
    return render(request, 'core/sobre-nosotros.html')

def catalogo(request):
    plantas = Producto.objects.all
    return render(request, "core/catalogo.html", {'plantas':plantas})

def logout(request):
    return logout_then_login(request, login_url="index")

def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/index.html')
    else:        
        form = Registro()
    return render(request, 'core/registro.html', {'form':form})


def suscribir(request):
    fecha = datetime.today().strftime('%d-%m-%Y')
    response = requests.get(f"https://mindicador.cl/api/dolar/{fecha}")
    dolar = float(response.json()["serie"][0]["valor"])
    plantas = Producto.objects.all()
    for planta in plantas:
        planta.endolares = round(planta.precio / dolar, 1)
    if not request.user.is_authenticated:
        return redirect('login')
    usuario = request.user
    correo = request.POST['correo']
    usuario_suscrito = Suscripcion.objects.values('user')
    suscrito = True
    if request.method == 'POST':
        if Suscripcion.objects.filter(user=usuario).exists():
            messages.error(request, "El usuario ya está suscrito!")
            return render(request, 'core/index.html', {'plantas':plantas, 'carro':request.session.get("carro",[])}) 
        else:
            usuarioapi = Suscripcion(user=usuario, correo_suscrito=correo, suscrito=suscrito)
            usuarioapi.save()
        return render(request, 'core/index.html', {'plantas':plantas, 'carro':request.session.get("carro",[])})
    

def eliminar_usuario(request, username):
    fecha = datetime.today().strftime('%d-%m-%Y')
    response = requests.get(f"https://mindicador.cl/api/dolar/{fecha}")
    dolar = float(response.json()["serie"][0]["valor"])
    plantas = Producto.objects.all()
    for planta in plantas:
        planta.endolares = round(planta.precio / dolar, 1)
    # Obtén el objeto Suscripcion correspondiente al usuario
    suscripcion = get_object_or_404(Suscripcion, user=username)

    if request.method == 'POST':
        # Elimina la suscripción de la base de datos
        suscripcion.delete()
        return render(request, 'core/index.html', {'plantas':plantas, 'carro':request.session.get("carro",[])})

    return render(request, 'core/eliminar_usuario.html', {'suscripcion': suscripcion})
