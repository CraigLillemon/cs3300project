# Generated by Django 5.0.3 on 2024-04-07 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0008_alter_state_state_alter_trail_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail_app.state'),
        ),
    ]