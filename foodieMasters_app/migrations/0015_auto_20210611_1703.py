# Generated by Django 2.2 on 2021-06-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodieMasters_app', '0014_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='users',
            new_name='user',
        ),
    ]