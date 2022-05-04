# Generated by Django 4.0.4 on 2022-05-03 06:26

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('entry_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('undated_date', models.DateTimeField(auto_now=True, null=True)),
                ('photo', models.ImageField(default='Capture.PNG', upload_to='images/profile_photo')),
                ('tag', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('contact', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(help_text='Enter your email addresses', max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('about', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Hobby', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Education', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Licenses_certifications', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Volunteering', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Skills', ckeditor.fields.RichTextField(blank=True, help_text='Enter a brief description of your skills', null=True)),
                ('Honors_awards', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Languages', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Organizations', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]