# Generated by Django 3.2.11 on 2022-05-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exams',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
