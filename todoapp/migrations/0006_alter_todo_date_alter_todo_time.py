# Generated by Django 4.0.4 on 2022-06-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Time',
            field=models.TimeField(auto_now=True),
        ),
    ]
