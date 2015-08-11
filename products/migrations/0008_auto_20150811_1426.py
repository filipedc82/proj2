# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150717_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='standard_alias',
            field=models.OneToOneField(related_name='standard_alias', blank=True, to='products.ProductAlias', null=True),
        ),
    ]
