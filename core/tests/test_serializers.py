from django.test import TestCase

from core.models import Task
from core.serializers import TaskSerializer


class TaskSerializerTestCase(TestCase):
    def test_ok(self):
        task_1 = Task.objects.create(name='task1', completed=False)
        task_2 = Task.objects.create(name='task2', completed=True)

        tasks = Task.objects.all()

        data = TaskSerializer(tasks, many=True).data

        expected_data = [
            {
                'id': task_1.id,
                'name': 'task1',
                'completed': False
            },
            {
                'id': task_2.id,
                'name': 'task2',
                'completed': True
            }
        ]
        self.assertEqual(expected_data, data)
