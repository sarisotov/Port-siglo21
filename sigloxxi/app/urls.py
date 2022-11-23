from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('carta', carta, name="carta"),
    path('registro/',registro,name="registro"),
    path('gestionar-bodega/',gestionar_bodega,name="gestionar_bodega"),
    path('base-trabajador/',base_trabajador,name="base_trabajador"),
    
    # CARRITO
    path('agregar/<int:id_plato>/', agregar_plato, name="Add"),
    path('eliminar/<int:id_plato>/', eliminar_plato, name="Del"),
    path('restar/<int:id_plato>/', restar_plato, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

    #CRUD

    # PLATOS
    path('gestionar-carta/',gestionar_carta,name="gestionar_carta"),
    path('eliminar-plato/<id_plato>',eliminar_plato,name="eliminar_plato"),
    path('modificar-plato/<id_plato>',modificar_plato,name="modificar_plato"),

    # PRODUCTOS
    path('gestionar-producto/',gestionar_producto,name="gestionar_producto"),
    path('eliminar-producto/<id_prod>',eliminar_producto,name="eliminar_producto"),
    path('modificar-producto/<id_prod>',modificar_producto,name="modificar_producto"),

    # MESAS
    path('gestionar-mesas/',gestionar_mesas,name="gestionar_mesas"),
    path('eliminar-mesas/<id_mesa>',eliminar_mesas,name="eliminar_mesas"),
    path('modificar-mesas/<id_mesa>',modificar_mesas,name="modificar_mesas"),
    

]
