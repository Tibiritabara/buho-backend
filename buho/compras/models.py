"""
Modelos de base de datos
"""
from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(
        "Nombre del contacto",
        max_length=100,
        null=False,
    )

    apellido = models.CharField(
        "Apellidos del contacto",
        max_length=200,
        null=False,
    )

    telefono = models.CharField(
        "Telefono del proveedor",
        max_length=20,
        null=False,
    )

    creado_en = models.DateTimeField(
        "Cuando fue creada la entrada.",
        auto_now_add=True,
    )

    actualizado_en = models.DateTimeField(
        "Cuando fue actualizada la entrada por ultima vez.",
        auto_now=True,
    )

    def __str__(self):
        return "{}, {}".format(
            self.apellido,
            self.nombre
        )


class Proveedor(models.Model):
    nombre = models.CharField(
        "Nombre del proveedor",
        max_length=200,
        null=False,
    )

    direccion = models.CharField(
        "Direccion del proveedor",
        max_length=500,
        null=False,
    )

    contacto = models.ForeignKey(
        Contacto,
        on_delete=models.CASCADE,
        related_name="contacto",
    )

    creado_en = models.DateTimeField(
        "Cuando fue creada la entrada.",
        auto_now_add=True,
    )

    actualizado_en = models.DateTimeField(
        "Cuando fue actualizada la entrada por ultima vez.",
        auto_now=True,
    )

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(
        "Nombre del articulo",
        max_length=500,
        null=False,
    )

    precio = models.FloatField(
        "Precio del articulo",
        null=False,
    )

    unidad = models.CharField(
        "Unidad del articulo",
        max_length=20,
        null=False,
    )

    marca = models.CharField(
        "Marca del articulo",
        max_length=500,
        null=True,
    )

    def __str__(self):
        return "{} - {}, {}/{}".format(
            self.marca,
            self.nombre,
            self.precio,
            self.unidad,
        )


class Compra(models.Model):
    total = models.FloatField(
        "Costo de la compra",
        null=False,
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name="proveedor",
    )

    creado_en = models.DateTimeField(
        "Cuando fue creada la entrada.",
        auto_now_add=True,
    )

    def __str__(self):
        return "{} - {}, {}".format(
            self.creado_en,
            self.proveedor,
            self.total,
        )


class Detalle(models.Model):
    cantidad = models.FloatField(
        "Cantidad de unidades del articulo",
        null=False,
    )

    articulo = models.ForeignKey(
        Articulo,
        on_delete=models.CASCADE,
        related_name="articulo",
    )

    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="compra",
    )

    def __str__(self):
        return "{} {} - {}".format(
            self.cantidad,
            self.articulo,
            self.compra,
        )
