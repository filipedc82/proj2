# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150630_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_no',
        ),
    ]
