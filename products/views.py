from django.views import generic
from django.contrib import messages
from extra_views import CreateWithInlinesView
from . import models
from . import forms

class ProductListView(generic.ListView):
    model = models.Product
    template_name = 'product_list.html'

class ProductAddView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_add.html'

class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
         context = super(ProductDetailView, self).get_context_data(**kwargs)
         fields = self.object._meta.fields
         values = [getattr(self.object, f.name) for f in fields]
         field_names = [f.verbose_name for f in fields]
         object_dict = dict(zip(field_names,values))
         context['object_dict'] = object_dict
         return context

class AliasAddView(generic.CreateView):
    model = models.ProductAlias
    form_class = forms.AliasForm
    template_name = 'alias_add.html'
    success_msg = "Alias successfully added!"

    def get_initial(self):
        return {'product': self.kwargs['product']}

    def get_success_url(self):
        return "/products/{0}/".format(self.kwargs['product'])

    def form_valid(self, form):
        messages.info(self.request, self.success_msg, 'alert-success' )
        return super(AliasAddView, self).form_valid(form)