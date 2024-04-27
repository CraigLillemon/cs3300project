# Generated by Django 5.0.3 on 2024-04-26 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_app', '0014_remove_trailfolder_trail_trail_trailfolder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailFolders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='trail',
            name='trailFolder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail_app.trailfolders'),
        ),
        migrations.AlterField(
            model_name='user',
            name='trailFolder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trail_app.trailfolders'),
        ),
        migrations.DeleteModel(
            name='TrailFolder',
        ),
    ]