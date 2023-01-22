# Generated by Django 4.1.5 on 2023-01-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('new', 'NEW'), ('done', 'DONE'), ('overdue', 'OVERDUE')], max_length=200),
        ),
    ]