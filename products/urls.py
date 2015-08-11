__author__ = 'Filipe'
from django.conf.urls import patterns, include, url
from . import views
# from django import views

#from .views import home_page, ProductListView, EngineCreateView


urlpatterns = patterns('',
    url(r'^$', views.ProductListView.as_view(), name='product_list'),
    )
