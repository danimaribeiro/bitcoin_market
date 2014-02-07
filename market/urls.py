from django.conf.urls import patterns, url

from market import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='market.index')
)