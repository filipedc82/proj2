from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.test.utils import override_settings
import sys

from core import utils

@override_settings(DEBUG=True)
class ProductsTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]  #4
                return  #5
        super().setUpClass()  #6
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
       # self.browser.quit()
        pass

    def test_can_see_products_list(self):
        #set up entry
        p1 = utils.createTestProduct()
        a1 = utils.createTestAlias(p1)
        a2 = utils.createTestAlias(p1)
        d1 = utils.createTestDrawing(a1)

        # Klaus enters the url and is shown a styled Products list page
        self.browser.get(self.server_url+ "/products/")
        self.assertIn('Product', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Product', header_text)
        self.assertGreater(self.browser.find_element_by_tag_name('h1').location['x'], 10)


        # In the list he sees one entry with a standard two alias
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn(p1.product_no, body_text)
        self.assertIn(a1.product_no, body_text)
        self.assertIn(a2.product_no, body_text)

        # He finds the link to create a new Product and  clicks it
        self.browser.find_element_by_id("add_product_link").click()
        # He is then shown a forms page and enters a Product No and clicks submit
        self.assertIn('Add new Product', self.browser.title)
        self.browser.find_element_by_id('id_product_no').send_keys("AnotherGuide")
        self.browser.find_element_by_id('submit-id-save').click()

        # He is then shown the product entry page
        self.assertIn('Product Details', self.browser.title)
        self.assertIn("AnotherGuide", self.browser.find_element_by_tag_name('body').text)

        # In the product detail page he sees a "add Alias" link and clicks it
        self.browser.find_element_by_id("add_alias_link").click()

        # He is shown a alias form page
        self.assertIn("Add Alias", self.browser.title)


        # In the detail page he clicks the "edit" link







        self.fail("So far so good! Finish the test!")




