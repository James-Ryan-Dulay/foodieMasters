# Generated by Django 2.2 on 2021-06-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodieMasters_app', '0008_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='recipe',
            field=models.TextField(default=0),
        ),
    ]
