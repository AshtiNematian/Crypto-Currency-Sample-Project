# Generated by Django 3.2.11 on 2022-07-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0015_auto_20220712_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='deploy/video/', verbose_name='video'),
        ),
    ]