# Generated by Django 3.2.11 on 2022-03-12 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_count', models.IntegerField(default=0)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='market.comment')),
                ('users', models.ManyToManyField(related_name='requirement_comment_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dislike_count', models.IntegerField(default=0)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dis_likes', to='market.comment')),
                ('users', models.ManyToManyField(related_name='requirement_comment_dis_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]