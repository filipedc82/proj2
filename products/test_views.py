from django.core.urlresolvers import resolve

from django_webtest import WebTest

from core import utils
from . import models

class ProductListViewWebTest(WebTest):

    def test_url_resolves_right_view(self):
        found = resolve('/products/')

        self.assertEqual(found.view_name, 'product_list')

    def test_renders_page(self):
        url="/products/"
        response = self.app.get(url)

        response.mustcontain("Product List")

    def test_displays_product(self):
        p1 = utils.createTestProduct()
        url="/products/"
        response = self.app.get(url)

        response.mustcontain(p1.product_no)


class ProductAddViewWebTest(WebTest):

    def test_url_resolves_right_view(self):
        found = resolve('/products/add/')

        self.assertEqual(found.view_name, 'product_add')

    def test_renders_page(self):
        url="/products/add/"
        response = self.app.get(url)

        response.mustcontain("Add new Product")

    def test_form_valid(self):
        url="/products/add/"
        response = self.app.get(url)
        form = response.form
        form['product_no'] = "Guide01"
        form['product_group'] = "VG"
        res = form.submit('save')

        self.assertRedirects(res, "/products/1/")
        self.assertEqual(models.Product.objects.count(), 1)

    def test_form_invalid(self):
        url="/products/add/"
        response = self.app.get(url)
        form = response.form
        form['product_no'] = ""
        res = form.submit('save')

        self.assertContains(res, "This field is required" )
        self.assertEqual(models.Product.objects.count(), 0)

    def test_form_forbids_double_entries(self):
        p = models.Product()
        p.product_no = "Guide01"
        p.save()

        url="/products/add/"
        response = self.app.get(url)
        form = response.form
        form['product_no'] = "Guide01"
        form['product_group'] = "VG"
        res = form.submit('save')

        self.assertContains(res, "already exists" )
        self.assertEqual(models.Product.objects.count(), 1)


class ProductDetailViewWebTest(WebTest):

    p = models.Product

    def setUp(self):
        self.p = models.Product()
        self.p.product_no = "Guide01"
        self.p.save()


    def test_url_resolves_right_view(self):
        found = resolve('/products/{0}/'.format(self.p.pk))
        self.assertEqual(found.view_name, 'product_detail')


    def test_renders_page(self):
        url = '/products/{0}/'.format(self.p.pk)
        response = self.app.get(url)

        response.mustcontain("Product Details")

    def test_add_alias_url_resolves_right_view(self):
        found = resolve('/products/{0}/'.format(self.p.pk) + 'add_alias/')
        self.assertEqual(found.view_name, 'alias_add')


    def test_add_alias_renders_page(self):
        url='/products/{0}/'.format(self.p.pk) + 'add_alias/'
        response = self.app.get(url)
        response.mustcontain("Add new Alias")

    def test_add_alias_forbids_double_entry(self):
        pa = utils.createTestAlias(self.p)
        url='/products/{0}/add_alias/'.format(self.p.pk)
        response = self.app.get(url)
        form = response.form
        form['product_no'] = pa.product_no
        form['vendor'] = "MWH"
        res = form.submit('save')

        self.assertEqual(models.ProductAlias.objects.count(), 1)
        self.assertContains(res, "already exists" )

    def test_add_alias_form_valid(self):
        url='/products/{0}/add_alias/'.format(self.p.pk)
        response = self.app.get(url)
        form = response.form
        form['product_no'] = "78.11.201"
        form['vendor'] = "MWH"
        res = form.submit('save')

        self.assertRedirects(res, "/products/{0}/".format(self.p.pk))
        self.assertEqual(models.ProductAlias.objects.count(), 1)

    def test_add_alias_form_invalid(self):
        url='/products/{0}/add_alias/'.format(self.p.pk)
        response = self.app.get(url)
        form = response.form
        form['product_no'] = "78.11.201"
        form['vendor'] = ""
        res = form.submit('save')

        self.assertContains(res, "This field is required" )
        self.assertEqual(models.ProductAlias.objects.count(), 0)
