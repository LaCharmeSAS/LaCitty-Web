# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Codigo del Pais')),
            ],
        ),
    ]