# Generated by Django 4.0.4 on 2022-04-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_like_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
