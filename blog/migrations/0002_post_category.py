# Generated by Django 3.2.11 on 2022-02-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('news', 'News'), ('latest signals', 'Latest Signals'), ('Key Fundamentals', 'Key Fundamentals'), ('Economic Reports', 'Economic Reports'), ('Patterns and Tools', 'Patterns and Tools'), ('academy', 'Academy')], default='unknown', max_length=20),
        ),
    ]