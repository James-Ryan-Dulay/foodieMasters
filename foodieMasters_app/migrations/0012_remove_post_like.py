# Generated by Django 2.2 on 2021-06-10 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodieMasters_app', '0011_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
