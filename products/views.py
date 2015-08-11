from django.views import generic
from . import models

class ProductListView(generic.ListView):
    model = models.Product
    template_name = 'product_list.html'