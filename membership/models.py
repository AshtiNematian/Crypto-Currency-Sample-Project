from datetime import datetime
from django.db import models

MEMBERSHIP_CHOICES = (
    ('6 Month', '6_month'),
    ('12 Month', '12_month'),
    ('1 Month(Free)', 'free')
)


class Membership(models.Model):
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Free',
        max_length=30)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=3)
    description = models.TextField(default='aaa')
    image = models.ImageField(default='image', upload_to='media')

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_membership')
    membership = models.ForeignKey(Membership, on_delete=models.DO_NOTHING, null=False, related_name='membership',
                                   default='1')
    date_of_membership = models.DateTimeField(default=datetime.now)
    date_create = models.DateTimeField(default=datetime.now)

    @property
    def age(self):
        return self.date_of_membership - self.date_create

    def __str__(self):
        return self.user.email


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.email
