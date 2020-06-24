from django import forms

from compras.models import Articulo, Compra, Contacto, Detalle, Proveedor

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            "nombre",
            "precio",
            "unidad",
            "marca",
        ]


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            "nombre",
            "apellido",
            "telefono",
        ]


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            "nombre",
            "direccion",
            "contacto",
        ]


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [
            "total",
            "proveedor",
        ]


class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = [
            "cantidad",
            "articulo",
            "compra",
        ]
