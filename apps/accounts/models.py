# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(max_length=32)

    class Meta:
        verbose_name = u'角色'
        verbose_name_plural = u'角色列表'
        ordering = ['id']

    def __unicode__(self):
        return self.role


class Profile(models.Model):
    PRIVILEGE_CHOICES = (
        (1, u'普通'),
        (2, u'中级'),
        (3, u'高级'),
        (4, u'超级'),
    )
    user = models.OneToOneField(User)
    role = models.ForeignKey(Role, verbose_name=u'角色')
    privilege = models.IntegerField(choices=PRIVILEGE_CHOICES, default=1, verbose_name=u'权限')

    class Meta:
        verbose_name = u'附加信息'
        verbose_name_plural = u'附加信息列表'
        ordering = ['id']

    def __unicode__(self):
        return 'the extra profile of %s' % self.user.get_full_name()
