# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Role, Profile


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


# Define an inline admin descriptor for UserCredit model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = u'附加信息列表'


# Define a new User admin
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'first_name', 'last_name', 'role', 'email', 'is_staff')
    ordering = ('username',)
    list_filter = ('is_staff', 'profile__role__role')

    def role(self, obj):
        return obj.profile.role.role
    role.short_description = u'角色'


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
