# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_product_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='standard_alias',
            field=models.ForeignKey(default=15, related_name='standard_alias', to='products.ProductAlias'),
            preserve_default=False,
        ),
    ]
