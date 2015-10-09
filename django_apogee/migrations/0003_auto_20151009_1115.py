# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_apogee', '0002_auto_20150923_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individu',
            name='lib_vil_nai_etu',
            field=models.CharField(max_length=40, null=True, verbose_name='lib', db_column='LIB_VIL_NAI_ETU'),
        ),
    ]
