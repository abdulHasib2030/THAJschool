# Generated by Django 4.2.6 on 2023-11-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_addcourses_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcourses',
            name='course_video',
            field=models.FileField(blank=True, upload_to='teacher/course-video/'),
        ),
    ]
