# Generated by Django 3.2.11 on 2022-03-12 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0005_alter_portfolio_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='market.assets')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]