from django.conf.urls import patterns, include, url
from order.views import OrderList

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^market/', include('market.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^configuration/', include('configuration.urls')),
    url(r'^$', 'market.views.home' , name='home'),
    url(r'^graph_api/', include('graph_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
