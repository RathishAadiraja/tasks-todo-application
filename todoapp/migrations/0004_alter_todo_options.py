# Generated by Django 4.0.3 on 2022-04-10 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['is_completed', 'task_deadline']},
        ),
    ]
