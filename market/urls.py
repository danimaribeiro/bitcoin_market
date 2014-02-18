from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from market import views

urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'market/login.html'}, name='market_login'),
    url(r'^logout', 'django.contrib.auth.views.logout_then_login', name='market_logout'),        
    url(r'^graficos/$', views.Graficos, name='market_graficos'),
    url(r'^(?P<coin>\w+)/$', views.index, name='market_index')    
)