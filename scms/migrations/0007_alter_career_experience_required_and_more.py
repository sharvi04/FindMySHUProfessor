# Generated by Django 4.2.15 on 2024-12-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scms', '0006_career_alter_page_page_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='experience_required',
            field=models.CharField(choices=[('6 Months', '6 Months'), ('1 Year', '1 Year'), ('1.5 Year', '1.5 Year'), ('2 Years', '2 Years')], help_text="Relevant experience (e.g., '1 year and above')", max_length=100),
        ),
        migrations.AlterField(
            model_name='career',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship')], help_text='Type of job', max_length=255),
        ),
        migrations.AlterField(
            model_name='career',
            name='qualifications',
            field=models.CharField(choices=[('B. SC Computers', 'B. SC Computers'), ('B. Tech CSC', 'B. Tech CSC')], help_text='Type of job', max_length=255),
        ),
    ]
