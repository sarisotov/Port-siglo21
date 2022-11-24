from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = ['nom_plato', 'descripcion', 'valor_plato', 'Imagen']
    nom_plato = forms.CharField(max_length=49, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre del plato'}), label='Nombre del Plato')
    descripcion = forms.CharField(max_length=49, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Descripción'}), label='Descripción')
    valor_plato = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Valor del plato'}), label='Precio')
    Imagen = forms.ImageField()

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = ['username',"first_name","last_name","password1","password2","groups" ]
                
    

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nom_prod','stock','tipo','estado','stock_min','costo']
    nom_prod = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}), 
        label='Nombre del Producto')
    stock = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Stock'}), 
        label='Stock')
    tipo = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tipo del Producto'}), 
        label='Tipo del Producto')
    stock_min = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Stock Minimo'}), 
        label='Stock Minimo')
    costo = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Costo del Producto'}), 
        label='Costo del Producto')
    

class MesasForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ['descripcion','max_pers','estadoMesa']
    descripcion = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Descripcion de la Mesa'}), 
        label='Descripcion de la Mesa')
    max_pers = forms.CharField(max_length=2, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Capacidad de la Mesa'}), 
        label='Capacidad de la Mesa')
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nom_prov','mail','fono','direccion']
    nom_prov = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre del Proveedor'}), 
        label='Nombre del Proveedor')
    mail = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo'}), 
        label='Correo')
    fono = forms.CharField(min_length=8, max_length=12, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Celular Proveedor'}), 
        label='Celular Proveedor')
    direccion = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Direccion del Proveedor'}), 
        label='Direccion del Proveedor')




"""
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombre','perfil')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            ),
            'perfil': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            )
        }

    def clean_password2(self):
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

"""
