#from extra_views import InlineFormSet

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Hidden

from . import models

# class ProductAliasInlines(InlineFormSet):
#     model = models.ProductAlias


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['product_no','product_group', 'oem','engine', 'side', 'flavor', 'description']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'save'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'id_product_form'

class AliasForm(forms.ModelForm):
    class Meta:
        model = models.ProductAlias
        fields = ['product', 'vendor', 'product_no', 'description']

    def __init__(self, *args, **kwargs):
        super(AliasForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'id_alias_form'
        self.helper.layout = Layout(
            Fieldset(
                'Enter Alias for Product',
#                Field('product', disabled=True),
                Field('product', readonly=True),
                'vendor',
                'product_no',
                'description',
            )
        )
        self.helper.layout.append(Submit('save', 'save'))
