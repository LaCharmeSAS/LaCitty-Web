# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Pais, Departamento
# Register your models here.


class paisAdmin(admin.ModelAdmin):
    list_display = ['idPais','nombre']
    list_filter = ['idPais','nombre']
    search_fields = ['idPais','nombre']

class departamentoAdmin(admin.ModelAdmin):
    raw_id_fields = ['idPais']
    list_display = ['idDepartamento','nombre']
    list_filter = ['idDepartamento','nombre']
    search_fields = ['idDepartamento','nombre']

admin.site.register(Pais, paisAdmin)
admin.site.register(Departamento, departamentoAdmin)