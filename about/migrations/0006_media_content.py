# Generated by Django 3.2.10 on 2021-12-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_rename_video_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
