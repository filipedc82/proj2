# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150717_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='standard_alias',
            field=models.OneToOneField(blank=True, related_name='standard_alias', to='products.ProductAlias'),
        ),
    ]
