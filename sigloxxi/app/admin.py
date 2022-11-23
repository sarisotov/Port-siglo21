from django.contrib import admin
from .models import *
# Register your models here.


class PlatoAdmin (admin.ModelAdmin):
    list_display = ["nom_plato", "valor_plato", "descripcion"]
    list_editable = ["valor_plato"]
    search_fields = ["nom_plato"]

admin.site.register(Plato, PlatoAdmin)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(LineaPedido)