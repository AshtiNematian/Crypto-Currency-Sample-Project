# Generated by Django 3.2.11 on 2022-03-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(default='portfolio', max_length=50, null=True, unique=True),
        ),
    ]
