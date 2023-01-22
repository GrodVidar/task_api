from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, UpdateAPIView, ListAPIView
from .models import Task, Person
from .serializers import TaskSerializer, PersonSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonTasksView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        person_id = self.kwargs['pk']
        return Task.objects.filter(person_id=person_id)


class PersonTasksStatusView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        person_id = self.kwargs['pk']
        status = self.kwargs['status']
        return Task.objects.filter(person_id=person_id).filter(status=status)
