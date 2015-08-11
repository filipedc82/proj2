# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('product_no', models.TextField(max_length=50)),
                ('status', models.CharField(max_length=50, choices=[('A', 'Active'), ('D', 'Draft'), ('O', 'Obsolete')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('vendor', models.TextField(max_length=200)),
                ('product_no', models.TextField(max_length=50)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='drawing',
            name='product_alias',
            field=models.ForeignKey(to='products.ProductAlias'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='engine',
            field=models.TextField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='oem',
            field=models.TextField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='side',
            field=models.CharField(max_length=50, choices=[('IN', 'Inlet'), ('EX', 'Exhaust'), ('IN/EX', 'Inlet/Exhaust')], blank=True),
            preserve_default=True,
        ),
    ]
