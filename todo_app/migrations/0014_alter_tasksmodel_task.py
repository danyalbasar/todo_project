# Generated by Django 3.2.6 on 2021-09-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0013_rename_fbmodel_feedbackmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='task',
            field=models.TextField(),
        ),
    ]
