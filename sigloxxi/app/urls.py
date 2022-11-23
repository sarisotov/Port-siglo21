from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('carta', carta, name="carta"),
    path('gestionar-carta/',gestionar_carta,name="gestionar_carta"),
    path('eliminar-plato/<id_plato>',eliminar_plato,name="eliminar_plato"),
    path('modificar-plato/<id_plato>',modificar_plato,name="modificar_plato"),
    path('registro/',registro,name="registro"),
    path('gestionar-bodega/',gestionar_bodega,name="gestionar_bodega"),
    path('base-trabajador/',base_trabajador,name="base_trabajador"),
    
    # CARRITO
    path('agregar/<int:id_plato>/', agregar_plato, name="Add"),
    path('eliminar/<int:id_plato>/', eliminar_plato, name="Del"),
    path('restar/<int:id_plato>/', restar_plato, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    

]
