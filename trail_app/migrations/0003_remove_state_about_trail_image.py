# Generated by Django 5.0.3 on 2024-04-07 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0002_rename_portfolio_trail_state_alter_state_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='about',
        ),
        migrations.AddField(
            model_name='trail',
            name='image',
            field=models.ImageField(default='', upload_to='static/images/'),
            preserve_default=False,
        ),
    ]
