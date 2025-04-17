# Generated by Django 5.1.2 on 2025-04-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_store', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('phone_store', models.IntegerField(max_length=20)),
                ('image_baner', models.CharField(blank=True, max_length=120)),
                ('image_horizontal', models.CharField(blank=True, max_length=120)),
                ('image_vertical', models.CharField(blank=True, max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
    ]
