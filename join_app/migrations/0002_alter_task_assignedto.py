# Generated by Django 5.1.4 on 2025-01-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignedTo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
