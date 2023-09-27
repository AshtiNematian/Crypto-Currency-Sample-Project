from rest_framework import serializers

from market.models import Assets


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['id', 'name', 'price', 'image']
