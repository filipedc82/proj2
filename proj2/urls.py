from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^products/', include('products.urls'), name='product_list'),
    url(r'^admin/', include(admin.site.urls)),
)
