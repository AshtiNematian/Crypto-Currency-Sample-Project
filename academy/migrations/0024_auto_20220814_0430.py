# Generated by Django 3.2.11 on 2022-08-14 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0023_auto_20220814_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='academy.teacher'),
        ),
        migrations.AddField(
            model_name='mycourseslist',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='academy.teacher'),
        ),
    ]