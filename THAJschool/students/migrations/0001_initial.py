# Generated by Django 4.2.3 on 2023-09-20 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('payment_method', models.CharField(max_length=100)),
                ('enroll_date', models.DateField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('Varified', 'Varified'), ('Unvarified', 'Unvarified')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='studentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_img', models.ImageField(blank=True, null=True, upload_to='images/student/profile/')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('street_address', models.CharField(blank=True, max_length=200, null=True)),
                ('education_level', models.CharField(blank=True, choices=[('', ''), ('JSC/ JDC/ 8 pass', 'JSC/ JDC/ 8 pass'), ('Secondary', 'Secondary'), ('Higher Secondary', 'Higher Secondary'), ('Diploma', 'Diploma'), ('Honous', 'Honurs'), ('Masters', 'Masters'), ('PhD(Doctor or Philosophy)', 'PhD(Doctor or Philosophy)')], max_length=200, null=True)),
                ('institute', models.CharField(blank=True, max_length=150, null=True)),
                ('passing_year', models.DateField(blank=True, null=True)),
                ('certificate', models.ImageField(blank=True, upload_to='images/student/certificate/')),
                ('course_history', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.coursehistory')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_account', to='accounts.student')),
            ],
        ),
    ]
