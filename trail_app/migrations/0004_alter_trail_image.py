# Generated by Django 5.0.3 on 2024-04-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0003_remove_state_about_trail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
