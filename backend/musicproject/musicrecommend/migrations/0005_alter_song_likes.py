# Generated by Django 4.2.4 on 2024-01-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_userlike_liked_on_alter_userlike_song_and_more'),
        ('musicrecommend', '0004_rename_id_song_song_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(related_name='song_likes', through='api.UserLike', to='api.customuser'),
        ),
    ]
