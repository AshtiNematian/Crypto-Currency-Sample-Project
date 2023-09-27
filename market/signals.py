from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from market.models import Portfolio, Market


@receiver(post_save, sender=User)
def create_user_portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(user=instance)


# @receiver(post_save, sender=Market)
def save_user_portfolio(sender, instance, **kwargs):
    post_save.disconnect(save_user_portfolio, sender=sender)
    instance.save()
    post_save.connect(save_user_portfolio, sender=sender)


post_save.connect(save_user_portfolio, sender=Market)
