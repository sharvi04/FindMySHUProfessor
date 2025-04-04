# Generated by Django 4.2.15 on 2024-12-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('navigation_text', models.CharField(max_length=255)),
                ('page_title', models.CharField(max_length=255)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('main_header', models.CharField(max_length=255)),
                ('sub_header', models.CharField(blank=True, max_length=255)),
                ('enable_gallery', models.BooleanField(default=False)),
                ('enable_uploads', models.BooleanField(default=False)),
                ('page_type', models.CharField(choices=[], max_length=50)),
                ('link_text', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_body', models.TextField(blank=True, null=True)),
                ('rich_intro', models.TextField(blank=True, null=True)),
                ('rich_body', models.TextField(blank=True, null=True)),
                ('teaser', models.TextField(blank=True, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('main_body', models.TextField(blank=True, null=True)),
                ('body1', models.TextField(blank=True, null=True)),
                ('body2', models.TextField(blank=True, null=True)),
                ('body3', models.TextField(blank=True, null=True)),
                ('body4', models.TextField(blank=True, null=True)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='uploads/thumbs/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='uploads/banners/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('seo_banner', models.ImageField(blank=True, null=True, upload_to='uploads/seo_banners/')),
                ('attachment1', models.ImageField(blank=True, null=True, upload_to='uploads/attachments/')),
                ('attachment2', models.ImageField(blank=True, null=True, upload_to='uploads/attachments/')),
                ('cta_header', models.CharField(blank=True, max_length=255, null=True)),
                ('cta_body', models.TextField(blank=True, null=True)),
                ('cta_action_text', models.CharField(blank=True, max_length=255, null=True)),
                ('cta_link_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(choices=[], max_length=255)),
                ('group', models.CharField(choices=[], max_length=50)),
                ('page_layout', models.CharField(choices=[], max_length=50)),
                ('published_on', models.DateField()),
                ('published', models.BooleanField(default=False)),
                ('expires_on', models.DateField(blank=True, null=True)),
                ('content_access_level', models.CharField(choices=[], max_length=50)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
