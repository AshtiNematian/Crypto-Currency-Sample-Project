# Generated by Django 3.2.11 on 2022-07-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_remove_assets_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]