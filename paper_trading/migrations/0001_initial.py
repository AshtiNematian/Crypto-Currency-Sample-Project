# Generated by Django 3.2.11 on 2022-06-27 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0014_alter_assets_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperTrading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('OPENED', 'opened'), ('CLOSED', 'closed')], default='opened', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('closed_at', models.DateTimeField()),
                ('side', models.CharField(choices=[('BUY', 'buy'), ('SELL', 'sell')], default='BUY', max_length=10)),
                ('assets', models.ManyToManyField(related_name='trading_assets', to='market.Assets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]