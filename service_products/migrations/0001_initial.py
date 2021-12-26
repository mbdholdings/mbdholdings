# Generated by Django 3.2.9 on 2021-12-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'Impression',
                'verbose_name_plural': 'Impression',
            },
        ),
        migrations.CreateModel(
            name='ServiceFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='service_products/')),
            ],
            options={
                'verbose_name': 'service five',
                'verbose_name_plural': 'service five',
            },
        ),
        migrations.CreateModel(
            name='ServiceFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='service_products/')),
            ],
            options={
                'verbose_name': 'service four',
                'verbose_name_plural': 'service four',
            },
        ),
        migrations.CreateModel(
            name='ServiceOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='service_products/')),
            ],
            options={
                'verbose_name': 'service one',
                'verbose_name_plural': 'service one',
            },
        ),
        migrations.CreateModel(
            name='ServiceSix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='service_products/')),
            ],
            options={
                'verbose_name': 'service six',
                'verbose_name_plural': 'service six',
            },
        ),
        migrations.CreateModel(
            name='ServiceThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='service_products/')),
            ],
            options={
                'verbose_name': 'service three',
                'verbose_name_plural': 'service three',
            },
        ),
        migrations.CreateModel(
            name='ServiceTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='service_products/')),
            ],
            options={
                'verbose_name': 'service two',
                'verbose_name_plural': 'service two',
            },
        ),
        migrations.CreateModel(
            name='Sliding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_big', models.CharField(blank=True, max_length=100)),
                ('description_small', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
            },
        ),
    ]