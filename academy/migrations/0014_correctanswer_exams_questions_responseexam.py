# Generated by Django 3.2.11 on 2022-06-20 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0013_auto_20220614_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('position', models.IntegerField(null=True, verbose_name='position')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
                ('option_a', models.CharField(default='a', max_length=100)),
                ('option_b', models.CharField(default='b', max_length=100)),
                ('option_c', models.CharField(default='c', max_length=100)),
                ('option_d', models.CharField(default='d', max_length=100)),
                ('position', models.IntegerField(default=1, verbose_name='position')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='academy.exams')),
            ],
            options={
                'ordering': ('position',),
                'unique_together': {('question', 'position')},
            },
        ),
        migrations.CreateModel(
            name='ResponseExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('score', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.exams')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='academy.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_response', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'exam', 'question')},
            },
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.exams')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='academy.questions')),
            ],
            options={
                'unique_together': {('exam', 'question', 'answer')},
            },
        ),
    ]