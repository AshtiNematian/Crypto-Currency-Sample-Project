# Generated by Django 3.2.11 on 2022-07-17 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_trading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papertrading',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]