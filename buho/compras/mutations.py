import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from compras.models import Articulo, Compra, Contacto, Detalle, Proveedor
from compras.forms import (
    ArticuloForm,
    CompraForm,
    ContactoForm,
    DetalleForm,
    ProveedorForm,
)


class ArticuloType(DjangoObjectType):
    class Meta:
        model = Articulo


class ArticuloMutation(DjangoModelFormMutation):
    articulo = graphene.Field(ArticuloType)

    class Meta:
        form_class = ArticuloForm


class CompraType(DjangoObjectType):
    class Meta:
        model = Compra


class CompraMutation(DjangoModelFormMutation):
    compra = graphene.Field(CompraType)

    class Meta:
        form_class = CompraForm


class DetalleType(DjangoObjectType):
    class Meta:
        model = Detalle


class DetalleMutation(DjangoModelFormMutation):
    detralle = graphene.Field(DetalleType)

    class Meta:
        form_class = DetalleForm


class ContactoType(DjangoObjectType):
    class Meta:
        model = Contacto


class ContactoMutation(DjangoModelFormMutation):
    contacto = graphene.Field(ContactoType)

    class Meta:
        form_class = ContactoForm


class ProveedorType(DjangoObjectType):
    class Meta:
        model = Proveedor


class ProveedorMutation(DjangoModelFormMutation):
    proveedor = graphene.Field(ProveedorType)

    class Meta:
        form_class = ProveedorForm


class Mutation(graphene.ObjectType):
    articulo = ArticuloMutation.Field()
    contacto = ContactoMutation.Field()
    proveedor = ProveedorMutation.Field()
    compra = CompraMutation.Field()
    detalle = DetalleMutation.Field()
