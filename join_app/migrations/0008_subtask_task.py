# Generated by Django 5.1.4 on 2025-01-14 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app', '0007_alter_subtask_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks_list', to='join_app.task'),
        ),
    ]
