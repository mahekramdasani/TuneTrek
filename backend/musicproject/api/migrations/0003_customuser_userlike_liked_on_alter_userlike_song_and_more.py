# Generated by Django 4.2.4 on 2024-01-19 21:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musicrecommend', '0004_rename_id_song_song_id'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0002_alter_userlike_song_alter_userlike_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='userlike',
            name='liked_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userlike',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicrecommend.song'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='userlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser'),
        ),
    ]