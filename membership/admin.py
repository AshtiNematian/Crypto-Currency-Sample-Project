from django.contrib import admin
from .models import Membership, UserMembership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'membership_type', 'price', 'image',)


class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'membership', 'date_of_membership', 'date_create')


admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
