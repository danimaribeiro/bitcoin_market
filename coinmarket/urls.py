from django.conf.urls import patterns, include, url
from market import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^market/', include('market.urls')),
    url(r'^$', views.OrderList.as_view() , name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
