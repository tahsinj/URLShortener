# Generated by Django 5.0.7 on 2024-08-03 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0003_rename_originial_url_shorturl_original_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturl',
            old_name='original_url',
            new_name='originial_url',
        ),
    ]