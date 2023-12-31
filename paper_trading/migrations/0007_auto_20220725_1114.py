# Generated by Django 3.2.11 on 2022-07-25 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_assets_price'),
        ('paper_trading', '0006_alter_papertrading_property_paper_trading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papertrading',
            name='assets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='paper_trading', to='market.assets'),
        ),
        migrations.AlterField(
            model_name='papertrading',
            name='property_paper_trading',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='paper_trading.propertypapertrading'),
        ),
    ]
