from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'accounts.views.index', name='index'),
    url(r'^(?P<username>[\.\w]+)/$', 'accounts.views.home', name='home'),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
