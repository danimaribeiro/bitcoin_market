from django.conf.urls import patterns, url

from market import views

urlpatterns = patterns('',
    url(r'^(?P<coin>\w+)/$', views.index, name='market.index')
)