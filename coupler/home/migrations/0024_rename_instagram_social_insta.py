# Generated by Django 4.0.6 on 2023-02-02 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_rename_insta_social_instagram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='instagram',
            new_name='insta',
        ),
    ]