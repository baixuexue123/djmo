# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import LoginView, ResetPwdView, logout_view, profile_view, changepwd_done


urlpatterns = patterns('',

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^changepwd/$', ResetPwdView.as_view(), name='reset-pwd'),
    url(r'^changepwddone/$', changepwd_done, name='changepwddone'),
)
