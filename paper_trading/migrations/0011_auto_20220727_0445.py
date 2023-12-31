# Generated by Django 3.2.11 on 2022-07-27 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paper_trading', '0010_alter_propertypapertrading_average_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertypapertrading',
            name='register',
            field=models.CharField(choices=[('registered', 'registered'), ('Not registered', 'Not registered')], default='Not registered', max_length=30),
        ),
        migrations.AddField(
            model_name='propertypapertrading',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
