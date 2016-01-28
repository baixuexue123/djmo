# -*- coding: utf-8 -*-
"""
    模块说明文档
"""

# 标准库
import os
import sys
import json

# 第三方库
import scrapy
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import (
    View, TemplateView, CreateView, RedirectView, FormView,
    DetailView, DateDetailView, DeleteView, UpdateView
)

# 自定义模块
import custom_modules1
import custom_modules2


# 常量定义
THIS_IS_CONST1 = 0
THIS_IS_CONST2 = True
THIS_IS_CONST3 = [
    'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx',
    'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx',
]
THIS_IS_CONST4 = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
}


class ClassName(object):
    """
    类文档
    注意类各个方法定义的顺序
    """
    static_var1 = 0
    static_var2 = 'string'
    static_var3 = u'中文字符串'

    def __init__(self, *args, **kwargs):
        super(ClassName, self).__init__()

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

    @property
    def property_name(self):
        return 0

    def base_method(self):
        raise NotImplementedError(u'这个方法需要子类重写')

    def _private_method(self):
        pass

    def instance_method(self):
        pass


def function(a, b):
    """
    函数说明

    Usage::
        >>> from template_m import function
        >>> ret = function(1, 2)

    :param a: string 描述说明
    :param b: int 描述说明
    :rtype int
    :return 描述说明
    """
    return a + b


def foo_long(*args, **kwargs):
    return 0


def foo():
    """多参数函数的传参书写格式, 和类实例化的格式"""
    ret = foo_long(a=1, b=2, c=3, d=4,
                   e=5, f=6, g=7, h=8)
    # 类实例化,传多个参数的格式
    object_ = ClassName(
            a=1, b=2, c=3, d=4,
            e=5, f=6, g=7, h=8
    )
    return ret

# 注意模块的最后一行要有一个空行
