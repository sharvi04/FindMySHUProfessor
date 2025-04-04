# Generated by Django 4.2.15 on 2024-12-14 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='SelectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('parent_key', models.CharField(blank=True, max_length=100, null=True)),
                ('display_order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
            options={
                'verbose_name': 'SelectList',
                'verbose_name_plural': 'SelectLists',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('country', models.ForeignKey(limit_choices_to={'status': 'active'}, on_delete=django.db.models.deletion.CASCADE, to='setup.country')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('state', models.ForeignKey(limit_choices_to={'status': 'active'}, on_delete=django.db.models.deletion.CASCADE, to='setup.state')),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
                ('gst_tax_no', models.CharField(blank=True, max_length=255, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=255, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/logos/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='company/banners/')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='company/qr_codes/')),
                ('active', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=3)),
                ('address', models.TextField()),
                ('bank_details', models.TextField()),
                ('terms', models.TextField()),
                ('note', models.TextField()),
                ('footer', models.TextField()),
                ('country', models.ForeignKey(blank=True, limit_choices_to={'status': 'active'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.country')),
                ('district', models.ForeignKey(blank=True, limit_choices_to={'status': 'active'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.district')),
                ('state', models.ForeignKey(blank=True, limit_choices_to={'status': 'active'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.state')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('order', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('page_layout', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True)),
                ('seo_keywords', models.TextField(blank=True, null=True)),
                ('seo_description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='categories/thumbnails/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories/images/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='categories/banners/')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='setup.category')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('active', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('company', models.ForeignKey(limit_choices_to={'active': 'yes'}, on_delete=django.db.models.deletion.CASCADE, to='setup.company')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('district', models.ForeignKey(limit_choices_to={'status': 'active'}, on_delete=django.db.models.deletion.CASCADE, to='setup.district')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=100)),
                ('opening_balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_contact_number', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('bank_address', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.branch')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.company')),
            ],
        ),
    ]
