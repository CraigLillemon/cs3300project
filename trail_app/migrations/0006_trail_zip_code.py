# Generated by Django 5.0.3 on 2024-04-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0005_trail_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='zip_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
