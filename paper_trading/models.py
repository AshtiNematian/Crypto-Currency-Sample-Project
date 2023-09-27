import datetime

from django.db import models
from django.utils import timezone

from market.models import Assets


class PaperTrading(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, null=True)
    assets = models.ManyToManyField(Assets, through='PropertyPaperTrading')

    def __str__(self):
        return str(self.user)


class PropertyPaperTrading(models.Model):
    SIDE_CHOICES = (('BUY', 'buy'), ('SELL', 'sell'))
    STATUS = (('OPENED', 'opened'), ('CLOSED', 'closed'))
    REGISTER = (('registered', 'registered'), ('Not registered', 'Not registered'))

    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, null=True)
    average_price = models.FloatField(blank=False, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=1)
    status = models.CharField(choices=STATUS, max_length=20, default='opened')
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    side = models.CharField(max_length=4, choices=SIDE_CHOICES)
    assets = models.ForeignKey(Assets, null=True, on_delete=models.CASCADE)
    paper_trading = models.ForeignKey(PaperTrading, null=True, on_delete=models.CASCADE)
    register = models.CharField(choices=REGISTER, max_length=30, default="Not registered")

    def __str__(self):
        return "%s" % self.side
