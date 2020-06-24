"""
Application GraphQL Schema
"""
import graphene
from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from compras.models import Articulo, Compra, Contacto, Detalle, Proveedor


class ContactoNode(DjangoObjectType):
    class Meta:
        model = Contacto
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
            'apellido': ['exact', 'icontains', 'istartswith'],
            'telefono': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class ProveedorNode(DjangoObjectType):
    class Meta:
        model = Proveedor
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
            'direccion': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class ArticuloNode(DjangoObjectType):
    class Meta:
        model = Articulo
        filter_fields = {
            'nombre': ['exact', 'icontains', 'istartswith'],
            'marca': ['exact', 'icontains', 'istartswith'],
            'precio': ['exact', 'gte', 'lte'],
        }
        interfaces = (relay.Node, )


class CompraNode(DjangoObjectType):
    class Meta:
        model = Compra
        filter_fields = {
            'total': ['exact', 'gte', 'lte'],
        }
        interfaces = (relay.Node, )


class DetalleNode(DjangoObjectType):
    class Meta:
        model = Detalle
        filter_fields = {
            'cantidad': ['exact', 'gte', 'lte'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    contactos = DjangoFilterConnectionField(ContactoNode)
    proveedores = DjangoFilterConnectionField(ProveedorNode)
    articulos = DjangoFilterConnectionField(ArticuloNode)
    compras = DjangoFilterConnectionField(CompraNode)
    contactos = DjangoFilterConnectionField(ContactoNode)
