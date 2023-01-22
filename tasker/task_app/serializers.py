from rest_framework import serializers
from .models import Task, Person


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'status', 'person')


class PersonSerializer(serializers.ModelSerializer):
    open_tasks = serializers.SerializerMethodField()
    total_tasks = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ('id', 'name', 'open_tasks', 'total_tasks')

    def get_open_tasks(self, person):
        return Task.objects.filter(person_id=person.pk).exclude(status=Task.DONE).count()

    def get_total_tasks(self, person):
        return Task.objects.filter(person_id=person.pk).count()


