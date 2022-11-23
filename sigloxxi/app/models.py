from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()

class Plato (models.Model):
    id_plato = models.AutoField(primary_key=True)
    nom_plato = models.CharField(max_length=50)
    valor_plato = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    Imagen = models.ImageField(default = None, upload_to="platos", null=True)

    def __str__(self):
        return self.nom_plato

estado_pedido = [
    ['Pendiente Pago', "Pendiente Pago"],
    ['Cancelado', "Cancelado"],
    ['Confirmado', "Confirmado"],
    ['Preparando', "Preparando"],
    ['Pagado', "Pagado"],
    ['Atrasado', "Atrasado"]
    ]

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=estado_pedido, default='Pendiente Pago')
    

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*("cantidad"), output_field=FloatField())
        )["total"]
    
    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class LineaPedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id_plato=models.ForeignKey(Plato, on_delete=models.CASCADE)
    pedido_id=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.id_plato.nom_plato}'

    class Meta:
        db_table='lineapedidos'
        verbose_name='linea pedido'
        verbose_name_plural='lineas pedidos'
        ordering=['id']

#equis
class mesas(models.Model):
    id_mesa=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=80)
    max_pers=models.IntegerField()

    def __str__(self):
        return self.descripcion

class proveedor(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nom_prov=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    fono=models.IntegerField()
    direccion=models.CharField(max_length=100)

    def __str__(self):
        return self.nom_prov
     

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=50)  
    stock = models.CharField(max_length=50)  
    tipo = models.CharField(max_length=50) 
    estado = models.CharField(max_length=50)
    stock_min = models.IntegerField
    valor = models.IntegerField()

    def __str__(self):
        return self.nom_ing