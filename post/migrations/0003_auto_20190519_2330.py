# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-19 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190516_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi'),
        ),
    ]