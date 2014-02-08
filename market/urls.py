from django.conf.urls import patterns, url

from market import views

urlpatterns = patterns('',
    url(r'^$', views.OrderList.as_view(), name='order_list'),
    url(r'^new$', views.OrderCreate.as_view(), name='order_new'),
    url(r'^edit/(?P<pk>\d+)$', views.OrderUpdate.as_view(), name='order_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.OrderDelete.as_view(), name='order_delete'),
    url(r'^admin/$', views.admin, name='market_admin'),
    url(r'^(?P<coin>\w+)/$', views.index, name='market_index')    
)