# Generated by Django 3.2.11 on 2022-04-12 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20220404_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='portfolio',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.DO_NOTHING, related_name='portfolio', to='market.portfolio'),
            preserve_default=False,
        ),
    ]
