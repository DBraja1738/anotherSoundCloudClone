# Generated by Django 5.0.1 on 2024-01-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicPlayer', '0002_song_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listen_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
