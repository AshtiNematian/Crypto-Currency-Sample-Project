# Generated by Django 3.2.11 on 2022-07-25 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper_trading', '0005_alter_papertrading_property_paper_trading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papertrading',
            name='property_paper_trading',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='paper_trading.propertypapertrading'),
        ),
    ]