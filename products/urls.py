__author__ = 'Filipe'
from django.conf.urls import patterns, include, url
from . import views
# from django import views

#from .views import home_page, ProductListView, EngineCreateView


urlpatterns = patterns('',
    url(r'^add/$', views.ProductAddView.as_view(), name='product_add'),
    url(r'^(?P<product>\d+)/add_alias/$', views.AliasAddView.as_view(), name='alias_add'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^$', views.ProductListView.as_view(), name='product_list'),
    )
