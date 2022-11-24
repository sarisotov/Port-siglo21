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
    platos = Plato.objects.all()
    return render(request, "carta", {'platos':platos})

@permission_required('app.view_plato')
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

@permission_required('app.view_user')
def listarUsuarios (request):
    user = User.objects.all()
    data = {
        'user': user
    }
    return render(request, 'registration/listarUss.html', data)


##################### CRUD #####################

####  CARTA  ####
@permission_required('app.add_plato')
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
@permission_required('app.change_plato')
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
@permission_required('app.delete_plato')
def eliminar_plato(request,id_plato):
    
    plato = get_object_or_404(Plato, id_plato=id_plato)
    plato.delete()
    messages.success(request, "Plato Eliminado Correctamente")
    return redirect(to="gestionar_carta")

#### PRODUCTO ####
@permission_required('app.add_producto')
def gestionar_producto(request):
    
    producto = Producto.objects.all()
    data = {
        'producto':producto,
        'form':ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correctamente")
        else:
            data["form"] = formulario


    return render(request, 'app/admin/producto/agregarProducto.html',data)
@permission_required('app.change_producto')
def modificar_producto(request,id_prod):
    
    producto = get_object_or_404(Producto, id_prod=id_prod)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(
            data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Modificado Correctamente")
            return redirect(to="gestionar_producto")
        else:
            data["form"] = formulario

    return render(request, 'app/admin/producto/modificarProducto.html', data)
@permission_required('app.delete_producto')
def eliminar_producto(request,id_prod):
    
    producto = get_object_or_404(Producto, id_prod=id_prod)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")
    return redirect(to="gestionar_producto")

#### MESA ####
@permission_required('app.add_mesas')
def gestionar_mesas(request):
    
    mesas = Mesas.objects.all()
    data = {
        'mesas':mesas,
        'form':MesasForm
    }

    if request.method == 'POST':
        formulario = MesasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mesa Agregado Correctamente")
        else:
            data["form"] = formulario


    return render(request, 'app/admin/mesas/agregarMesa.html',data)
@permission_required('app.change_mesas')
def modificar_mesas(request,id_mesa):
    
    mesas = get_object_or_404(Mesas, id_mesa=id_mesa)

    data = {
        'form': MesasForm(instance=mesas)
    }

    if request.method == 'POST':
        formulario = MesasForm(
            data=request.POST, instance=mesas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mesa Modificado Correctamente")
            return redirect(to="gestionar_mesas")
        else:
            data["form"] = formulario

    return render(request, 'app/admin/mesas/modificarMesa.html', data)
@permission_required('app.delete_mesas')
def eliminar_mesas(request,id_mesa):
    
    mesas = get_object_or_404(Mesas, id_mesa=id_mesa)
    mesas.delete()
    messages.success(request, "Mesa Eliminado Correctamente")
    return redirect(to="gestionar_mesas")

### PROVEEDORES ###
@permission_required('app.add_proveedor')
def gestionar_proveedores(request):
    
    proveedor = Proveedor.objects.all()
    data = {
        'proveedor':proveedor,
        'form':ProveedorForm
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor Agregado Correctamente")
        else:
            data["form"] = formulario


    return render(request, 'app/admin/proveedor/agregarProveedor.html',data)
@permission_required('app.change_proveedor')
def modificar_proveedores(request,id_prov):
    
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(
            data=request.POST, instance=proveedor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor Modificado Correctamente")
            return redirect(to="gestionar_proveedores")
        else:
            data["form"] = formulario

    return render(request, 'app/admin/proveedores/modificarProveedor.html', data)
@permission_required('app.delete_proveedor')
def eliminar_proveedores(request,id_prov):
    
    proveedor = get_object_or_404(Proveedor, id_prov=id_prov)
    proveedor.delete()
    messages.success(request, "Proveedor Eliminado Correctamente")
    return redirect(to="gestionar_proveedores")


################################################




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

    return redirect(to="Pedidos")
