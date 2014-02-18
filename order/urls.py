from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from order.views import OrderList, OrderCreate, OrderUpdate, OrderDelete

urlpatterns = patterns('',
    url(r'^$', login_required(OrderList.as_view()), name='order_list'),
    url(r'^new$', login_required(OrderCreate.as_view()), name='order_new'),
    url(r'^edit/(?P<pk>\d+)$', login_required(OrderUpdate.as_view()), name='order_update'),
    url(r'^delete/(?P<pk>\d+)$', login_required(OrderDelete.as_view()), name='order_delete'),
)