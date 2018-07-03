# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Pais(models.Model):
    idPais = models.CharField(max_length=4, verbose_name="Codigo del Pais", blank=False, null=False, primary_key=True)
    nombre = models.CharField(max_length=45, verbose_name="Nombre del Pais", blank=False, null=False)

    class Meta:
        verbose_name_plural = "País"

    def __unicode__(self):
        return str(self.nombre)


class Departamento(models.Model):
    idDepartamento = models.AutoField(max_length=11, blank=False, null=False, primary_key=True)
    idPais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País",)
    nombre = models.CharField(max_length=45, verbose_name="Nombre del Departamento", blank=False, null=False)

    class Meta:
        verbose_name_plural = "Departamento"

    def __unicode__(self):
        return str(self.nombre)