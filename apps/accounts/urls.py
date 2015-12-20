# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import LoginView, ChangePasswordView, logout_view, profile_view, change_pwd_done


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^(?P<username>[\.\w]+)/profile/$', profile_view, name='profile'),
    url(r'^(?P<username>[\.\w]+)/changepwd/$', ChangePasswordView.as_view(), name='change_pwd'),
    url(r'^changepwddone/$', change_pwd_done, name='change_pwd_done'),
]
