from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from sec.models import LifeUser


class LifeUserInline(admin.StackedInline):
    model = LifeUser
    can_delete = False
    verbose_name_plural = 'LifeUser'


class UserAdmin(BaseUserAdmin):
    inlines = (LifeUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
