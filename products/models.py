from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


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
    product_no = models.CharField(max_length=50, unique=True, verbose_name="Product No.")
   # standard_alias = models.OneToOneField('products.ProductAlias', related_name='standard_alias', blank=True, null=True)
    product_group = models.CharField(max_length=50, choices=PRODUCT_GROUPS, default="O", verbose_name="Product Group")
    engine = models.CharField(max_length=50, blank=True, verbose_name="Engine")
    oem = models.CharField(max_length=50, blank=True, verbose_name="Engine OEM")
    side = models.CharField(max_length=50, choices=(('IN', 'Inlet'), ('EX', 'Exhaust'), ('IN/EX', 'Inlet/Exhaust')),
                            blank=True, verbose_name="Side")
    flavor = models.CharField(max_length=50, choices=(('STD', 'Standard'), ('OVZ', 'Oversize'), ('TUN', 'Tuning'),
                                                       ('OTH','Other')),
                            blank=True, verbose_name="Flavor")
    description = models.TextField(max_length=200, blank=True, verbose_name="Description")

    def __str__(self):
        return self.product_no

    def get_absolute_url(self):
        return "/products/%i/" % self.id



class ProductAlias(models.Model):
    product = models.ForeignKey(Product)
    vendor = models.TextField(max_length=200, verbose_name="Vendor")
    product_no = models.TextField(max_length=50, unique=True, verbose_name="Product No.")
    description = models.TextField(max_length=200, blank=True, verbose_name="Description")

    def __str__(self):
        return str(self.vendor + " " + self.product_no)

    def clean(self):
        """ make sure that the alias product no is not the same as the parent no """
        if self.product_no == self.product.product_no:
            msg = "Alias Part No. cannot be the same as its product`s"
            raise ValidationError(msg)
        super(ProductAlias,self).clean()

    def save(self, *args, **kwargs):
        """ force model to clean() """
        self.clean()
        super(ProductAlias, self).save(*args, **kwargs) # Call the "real" save() method.


class Drawing(models.Model):
    product = models.ForeignKey(Product)
    drawing_no = models.TextField(max_length=50)
    revision = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=(('A', 'Active'), ('D', 'Draft'), ('O', 'Obsolete')))
    drawing_file = models.FileField(upload_to="drawings", blank=True)


    class Meta:
        unique_together = ('drawing_no', 'revision')

    def __str__(self):
        return str(self.drawing_no)