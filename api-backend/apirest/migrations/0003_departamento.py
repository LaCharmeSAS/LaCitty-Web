# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0002_auto_20180703_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepartamento', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre del Departamento')),
            ],
            options={
                'verbose_name_plural': 'Departamento',
            },
        ),
    ]