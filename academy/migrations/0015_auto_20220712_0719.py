# Generated by Django 3.2.11 on 2022-07-12 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0014_correctanswer_exams_questions_responseexam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['-id']},
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='deploy/video/%Y//5m//%d/', verbose_name='course_video')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_videos', to='academy.courses')),
            ],
        ),
    ]
