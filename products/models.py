from django.db import models
from django.core.urlresolvers import reverse



class UnsavedForeignKey(models.ForeignKey):
    ### use until Django 1.8.4 makes this irrelevant
    allow_unsaved_instance_assignment = True


class Product(models.Model):
    PRODUCT_GROUPS = (
        ('VG', 'Valve Guide'),
        ('VS', 'Valve Seat'),
        ('EV', 'Engine Valve'),
        ('EVO', 'Engine Valve Other'),
        ('NGP', '(Normalien)Guide Pin'),
        ('NLS', '(Normalien)Limit Switch'),
        ('NLS', '(Normalien)Other'),
        ('O', 'Other'),
    )
    #    product_no = models.TextField(max_length=50)
    standard_alias = models.OneToOneField('products.ProductAlias', related_name='standard_alias', blank=True, null=True)
    product_group = models.CharField(max_length=50, choices=PRODUCT_GROUPS, default="O")
    engine = models.TextField(max_length=50, blank=True)
    oem = models.TextField(max_length=50, blank=True)
    side = models.CharField(max_length=50, choices=(('IN', 'Inlet'), ('EX', 'Exhaust'), ('IN/EX', 'Inlet/Exhaust')),
                            blank=True)


class ProductAlias(models.Model):
    product = models.ForeignKey(Product)
    vendor = models.TextField(max_length=200)
    product_no = models.TextField(max_length=50)

    def __str__(self):
        return str(self.vendor + " " + self.product_no)


class Drawing(models.Model):
    product_alias = models.ForeignKey(ProductAlias)
    drawing_no = models.TextField(max_length=50)
    status = models.CharField(max_length=50, choices=(('A', 'Active'), ('D', 'Draft'), ('O', 'Obsolete')))

    def __str__(self):
        return str(self.drawing_no)