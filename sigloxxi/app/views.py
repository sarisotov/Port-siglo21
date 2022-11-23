from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from app.Carrito import Carrito
from .forms import *
from .models import *

# Create your views here.

# CARRITO
def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    platos = Plato.objects.all()
    return render(request, "carta", {'platos':platos})

def agregar_plato(request, id_plato):
    carrito = Carrito (request)
    plato = Plato.objects.get(id_plato=id_plato)
    carrito.agregar(plato)
    return redirect ("carta")

def restar_plato(request, id_plato):
    carrito = Carrito(request)
    plato = Plato.objects.get(id_plato=id_plato)
    carrito.restar(plato)
    return redirect("carta")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carta")


def home (request):
    return render(request, 'app/home.html')

def base_trabajador(request):
    return render(request, 'app/admin/base-trabajador.html')

    
def carta (request):
    vplato = Plato.objects.all()
    data = {
        'platos': vplato
    }
    return render(request, 'app/carta.html', data)

def gestionar_carta(request):
    
    plato = Plato.objects.all()
    data = {
        'plato': plato,
        'form':PlatoForm
    }

    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Plato Agregado Correctamente")
        else:
            data["form"] = formulario


    return render(request, 'app/admin/carta/agregar.html',data)


def modificar_plato(request,id_plato):
    
    plato = get_object_or_404(Plato, id_plato=id_plato)

    data = {
        'form': PlatoForm(instance=plato)
    }

    if request.method == 'POST':
        formulario = PlatoForm(
            data=request.POST, instance=plato, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Plato Modificado Correctamente")
            return redirect(to="gestionar_carta")
        else:
            data["form"] = formulario

    return render(request, 'app/admin/carta/modificar.html', data)

def eliminar_plato(request,id_plato):
    
    plato = get_object_or_404(Plato, id_plato=id_plato)
    plato.delete()
    messages.success(request, "Plato Eliminado Correctamente")
    return redirect(to="gestionar_carta")



def registro(request):
    data={
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Completo")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)

def gestionar_bodega(request):
    plato = Plato.objects.all()
    data = {
        'plato': plato,
        'form':PlatoForm
    }

    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Plato Agregado Correctamente")
        else:
            data["form"] = formulario


    return render(request, 'app/admin/carta/gestionar-bodega.html',data)

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carrito = Carrito(request)
    lineas_pedido=list()
    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(
            id_plato=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    messages.success(request, "Pedido realizado")
