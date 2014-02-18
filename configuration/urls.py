from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from configuration.views import ConfigurationList, ConfigurationCreate, ConfigurationUpdate

urlpatterns = patterns('',
    url(r'^$', login_required(ConfigurationList.as_view()), name='configuration_list'),
    url(r'^new$', login_required(ConfigurationCreate.as_view()), name='configuration_new'),
    url(r'^edit/(?P<pk>\d+)$', login_required(ConfigurationUpdate.as_view()), name='configuration_update'),
)