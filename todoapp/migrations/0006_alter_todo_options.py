# Generated by Django 4.0.3 on 2022-04-18 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todo_task_deadline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['task_deadline', 'is_completed']},
        ),
    ]