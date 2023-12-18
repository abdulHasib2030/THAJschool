# Generated by Django 3.2.23 on 2023-12-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('teachers', '0003_addcourses_course_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_img', models.FileField(upload_to='teacher/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
            ],
        ),
    ]