from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.files import File as DjangoFile
from . import models
from core import utils

class ModelTest(TestCase):

    def test_can_add_and_retrieve_product(self):
        p1 = utils.createTestProduct()

        self.assertEqual(models.Product.objects.count(), 1)

        self.assertEqual(models.Product.objects.last().product_group,p1.product_group)

    def test_can_add_and_retrieve_alias(self):
        """
        Should two times create a product with an standard alias and a normal alias each
        """

        a1 = utils.createTestAlias()
        a2 = utils.createTestAlias()

        self.assertEqual(models.ProductAlias.objects.count(),2)
        self.assertEqual(models.ProductAlias.objects.last().vendor, a2.vendor)

    def test_add_alias_forbids_same_product_no_as_parent_product(self):

        p1 = utils.createTestProduct()

        with self.assertRaises(ValidationError):
            a1 = utils.createTestAlias(p1, p1.product_no)


    def test_can_add_and_retrieve_drawing(self):
        d1 = utils.createTestDrawing()
        d2 = utils.createTestDrawing()

        self.assertEqual(models.Drawing.objects.count(),2)
        self.assertEqual(models.Drawing.objects.last().drawing_no, d2.drawing_no)
        self.assertEqual(models.Drawing.objects.first().product, d1.product)

    def test_can_add_file_to_drawing(self):
        d1 = utils.createTestDrawing()
        df = DjangoFile(open("todo.txt", 'rb'))
        d1.drawing_file = df
        d1.save()
        print(models.Drawing.objects.first().drawing_file.name)
        self.assertEquals(models.Drawing.objects.first().drawing_file.name, "drawings/todo.txt")
        d1.drawing_file.delete()


    def test_forbids_two_drawings_with_same_no_and_revision(self):
        d1 = utils.createTestDrawing()
        d1.revision = 1
        d1.save()
        with self.assertRaises(IntegrityError):
            d2 = utils.createTestDrawing(d1.product, d1.drawing_no)
            d2.revision = d1.revision
            d2.save()

