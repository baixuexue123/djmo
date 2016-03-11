# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=24)
    password = forms.CharField(max_length=24)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.initial = self.initial or {'username': '', 'password': ''}


class ChangePasswordForm(forms.Form):
    password_current = forms.CharField(max_length=24)
    password_new = forms.CharField(max_length=24)
    password_new_confirm = forms.CharField(max_length=24)

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.initial = self.initial or {'password_current': '', 'password_new': '', 'password_new_confirm': ''}

    def clean_password_current(self):
        if not self.user.check_password(self.cleaned_data.get('password_current')):
            raise forms.ValidationError(u'原始密码错误')
        return self.cleaned_data['password_current']

    def clean_password_new_confirm(self):
        if 'password_new' in self.cleaned_data and 'password_new_confirm' in self.cleaned_data:
            if self.cleaned_data['password_new'] != self.cleaned_data['password_new_confirm']:
                raise forms.ValidationError(u'两次新密码不一致！')
        return self.cleaned_data['password_new_confirm']

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        print 'clean---------------------------'
