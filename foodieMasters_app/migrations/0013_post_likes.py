# Generated by Django 2.2 on 2021-06-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodieMasters_app', '0012_remove_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='like_post', to='foodieMasters_app.User'),
        ),
    ]
