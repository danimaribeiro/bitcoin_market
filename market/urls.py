from django.conf.urls import patterns, url

from market import views

urlpatterns = patterns('',
    url(r'^admin/$', views.admin, name='market.admin'),
    url(r'^(?P<coin>\w+)/$', views.index, name='market.index')    
)