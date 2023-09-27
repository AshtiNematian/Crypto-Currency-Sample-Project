# Generated by Django 3.2.11 on 2022-05-28 08:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_advicerequests_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advicerequests',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+989121111111', max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='courses',
            name='default_course',
            field=models.BooleanField(default=False),
        ),
    ]