from rest_framework import serializers

from membership.models import Membership, UserMembership


class MemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'membership_type', 'price','description','image']


class UserMemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembership
        fields = ['id', 'user', 'membership']
