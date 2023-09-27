from django.contrib import admin
from rest_framework_simplejwt import token_blacklist

from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'auth_provider', 'created_at', 'id', 'is_adviser']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'created_at']


class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)
