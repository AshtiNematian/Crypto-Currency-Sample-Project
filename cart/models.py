from django.db import models
from accounts.models import User
from membership.models import Membership


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=False)
    item = models.ForeignKey(Membership, on_delete=models.DO_NOTHING, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} ".format(self.user,
                                           self.item,
                                           self.created_at,
                                           self.updated_at)


class Coupon(models.Model):
    minimum_cart_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount_rate = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.minimum_cart_amount,
                                          self.discount_rate,
                                          self.created_at,
                                          self.updated_at)
