# Generated by Django 4.2.6 on 2023-11-27 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_addcourses_course_video'),
        ('enroll', '0002_courseenroll_student_courseenroll_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseenroll',
            name='teacher',
        ),
        migrations.AddField(
            model_name='courseenroll',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_name', to='teachers.addcourses'),
        ),
    ]
