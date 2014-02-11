from django.conf.urls import patterns, url
from graph_api import views

urlpatterns = patterns('',                           
    url(r'^chart$', views.time_series, name='graphapi_chart'),        
)