# Generated by Django 4.2.3 on 2023-09-20 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='addCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('available_courses', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('course_duration', models.CharField(max_length=50)),
                ('course_content', models.TextField(max_length=2000)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.teacher')),
            ],
        ),
    ]