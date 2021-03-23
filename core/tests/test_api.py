from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Task
from core.serializers import TaskSerializer


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task_1 = Task.objects.create(name='Task 1', completed=True)
        self.task_2 = Task.objects.create(name='Task 2')
        self.task_3 = Task.objects.create(name='Task 3', completed=False)

    def test_list(self):
        url = '/api/tasks/'
        response = self.client.get(url, format='json')

        tasks = Task.objects.all()
        serializer_data = TaskSerializer(tasks, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_retrieve(self):
        url = f'/api/tasks/{self.task_1.id}/'
        response = self.client.get(url, format='json')
        serializer_data = TaskSerializer(self.task_1).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Task.objects.all().count())
        url = '/api/tasks/'
        new_task = {'name': 'New Task'}

        response = self.client.post(url, data=new_task, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Task.objects.all().count())

    def test_update(self):
        url = f'/api/tasks/{self.task_1.id}/'
        response = self.client.patch(url, data={'completed': True}, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.task_1.refresh_from_db()
        self.assertTrue(self.task_1.completed)

    def test_delete(self):
        self.assertEqual(3, Task.objects.all().count())
        url = f'/api/tasks/{self.task_1.id}/'
        response = self.client.delete(url, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        self.assertEqual(2, Task.objects.all().count())
