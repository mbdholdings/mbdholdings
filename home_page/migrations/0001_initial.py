# Generated by Django 3.2.9 on 2021-12-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadingOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Heading_one',
                'verbose_name_plural': 'Heading_one',
            },
        ),
        migrations.CreateModel(
            name='HeadingThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Heading_three',
                'verbose_name_plural': 'Heading_three',
            },
        ),
        migrations.CreateModel(
            name='HeadingTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Heading_two',
                'verbose_name_plural': 'Heading_two',
            },
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'impression',
                'verbose_name_plural': 'impression',
            },
        ),
        migrations.CreateModel(
            name='MissionVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'mission vision',
                'verbose_name_plural': 'mission vision',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='home_page/')),
                ('text_one', models.TextField(blank=True, max_length=200)),
                ('text_two', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
            },
        ),
        migrations.CreateModel(
            name='WelcomeWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'welcome word',
                'verbose_name_plural': 'welcome words',
            },
        ),
    ]