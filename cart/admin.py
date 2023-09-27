from django.contrib import admin

from cart.models import Cart, Coupon


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'created_at', 'updated_at']


class CouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'minimum_cart_amount', 'discount_rate', 'created_at', 'updated_at']


admin.site.register(Cart, CartAdmin)
admin.site.register(Coupon, CouponAdmin)
