# Generated by Django 4.0.6 on 2022-07-27 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password',
            new_name='pass1',
        ),
    ]
