# Generated by Django 4.1 on 2022-08-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_talent_talentimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]