# Generated by Django 5.0.3 on 2024-04-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0006_trail_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='list_state',
            field=models.BooleanField(default=False),
        ),
    ]
