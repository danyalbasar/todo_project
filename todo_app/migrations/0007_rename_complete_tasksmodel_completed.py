# Generated by Django 3.2.6 on 2021-09-28 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_tasksmodel_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasksmodel',
            old_name='complete',
            new_name='completed',
        ),
    ]
