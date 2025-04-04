# Generated by Django 4.2.15 on 2024-12-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scms', '0008_alter_career_last_date_to_apply_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('apply_role', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='career',
            name='requirement',
            field=models.CharField(choices=[('Immediate', 'Immediate')], help_text="Urgency of the requirement (e.g., 'Immediate')", max_length=100),
        ),
    ]
