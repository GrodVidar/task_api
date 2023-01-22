from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task, Person
import json


class TaskTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(name="John Doe")
        self.task = Task.objects.create(title="Test task", person=self.person)
        self.valid_payload = {
            'title': 'Test task',
            'description': 'Test Description',
            'status': Task.DONE,
            'person': self.person.id
        }
        self.invalid_payload = {
            'title': '',
            'description': '',
            'status': Task.NEW,
            'person': ''
        }

    def test_get_all_tasks(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test task')

    def test_create_valid_task(self):
        response = self.client.post(
            reverse('task-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=response.data['id']).title, 'Test task')
