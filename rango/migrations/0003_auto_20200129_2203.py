# Generated by Django 2.2.3 on 2020-01-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]