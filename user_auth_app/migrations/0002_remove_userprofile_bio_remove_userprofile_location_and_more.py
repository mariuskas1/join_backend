# Generated by Django 5.1.4 on 2025-01-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='default', max_length=255),
        ),
    ]
