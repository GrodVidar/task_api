from django.db import models


class Task(models.Model):
    NEW = 'new'
    DONE = 'done'
    OVERDUE = 'overdue'
    STATUSES = [
        (NEW, 'New'),
        (DONE, 'Done'),
        (OVERDUE, 'Overdue')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUSES)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='tasks')


class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
