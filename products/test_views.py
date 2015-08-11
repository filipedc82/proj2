from django.core.urlresolvers import resolve

from django_webtest import WebTest

from core import utils

class ListViewWebTest(WebTest):

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
        response.mustcontain(p1.standard_alias.product_no)