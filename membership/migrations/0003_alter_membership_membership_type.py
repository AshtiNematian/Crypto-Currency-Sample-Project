# Generated by Django 3.2.11 on 2022-05-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_alter_membership_membership_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('6 Month', '6_month'), ('12 Month', '12_month')], default='Free', max_length=30),
        ),
    ]