# Generated by Django 3.2.6 on 2021-09-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_alter_tasksmodel_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksmodel',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
