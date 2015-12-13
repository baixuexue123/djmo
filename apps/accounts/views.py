# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def index(request):
    if request.user.is_authenticated():
        return redirect('/syndra/%s/' % request.user.username)
    else:
        return redirect('/accounts/login/')


class LoginView(TemplateView):

    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['username'] = request.POST.get('username')
        context['password'] = request.POST.get('password')

        if not all((context['username'], context['password'])):
            messages.info(request, u'用户名和密码不能为空！')
            return self.render_to_response(context)
        # 认证
        user = authenticate(username=context['username'], password=context['password'])
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/syndra/%s/' % user.username)
        else:
            messages.info(request, u'用户名或密码错误！')
            return self.render_to_response(context)


@login_required
def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/accounts/login/')


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def changepwd_done(request):
    return render(request, 'changepwd-done.html')


class ResetPwdView(LoginRequiredMixin, TemplateView):

    template_name = 'changepwd.html'

    def post(self, request, *args, **kwargs):
        context = super(ResetPwdView, self).get_context_data(**kwargs)
        context['old_pwd'] = request.POST.get('old-pwd')
        context['new_pwd'] = request.POST.get('new-pwd')
        context['new_pwd_again'] = request.POST.get('new-pwd-again')

        if not all((context['old_pwd'], context['new_pwd'], context['new_pwd_again'])):
            messages.info(request, u'填写信息不完整')
            return self.render_to_response(context)

        if context['new_pwd'] != context['new_pwd_again']:
            messages.info(request, u'两次输入密码不一样')
            return self.render_to_response(context)

        user = request.user
        if user.check_password(context['old_pwd']):
            user.set_password(context['new_pwd'])
            user.save()
            update_session_auth_hash(request, user)  # 修改密码不使session失效,从而退出登录
            return redirect('/accounts/changepwddone/')
        else:
            messages.info(request, u'原始密码不正确')
            return self.render_to_response(context)
