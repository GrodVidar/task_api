# Generated by Django 4.1.5 on 2023-01-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_person_task_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('done', 'Done'), ('overdue', 'Overdue')], max_length=200),
        ),
    ]