from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import User, VerificationOpt, UserAddress

# Register your models here.

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number')


@admin.register(VerificationOpt)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'expires_in')


@admin.register(UserAddress)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'street')
