# Generated by Django 2.2 on 2021-06-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodieMasters_app', '0003_auto_20210605_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
