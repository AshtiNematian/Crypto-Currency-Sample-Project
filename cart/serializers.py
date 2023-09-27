from rest_framework import serializers

from cart.models import Cart, Coupon


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'item', 'created_at', 'updated_at']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'minimum_cart_amount', 'discount_rate', 'created_at', 'updated_at']
