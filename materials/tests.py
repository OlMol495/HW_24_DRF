from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):
    """ Тесты на CRUD урока """

    def setUp(self):
        self.user = User.objects.create(email="test@admin.pro", password="admin")
        self.user2 = User.objects.create(email="test2@admin.pro", password="admin")
        self.lesson = Lesson.objects.create(
            title='Test',
            description='Test',
            owner=self.user
        )

    def test_create_lesson(self):
        """ Тесты на создание урока """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test1',
            'description': 'Test1'
        }
        response = self.client.post(
            reverse('materials:lesson-create'),
            data=data
        )

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверка на верность создаваемых полей
        self.assertEqual(
            response.json(),
            {
                'course': None,
                'title': 'Test1',
                'description': 'Test1',
                'id': 2,
                'image': None,
                'owner': 1,
                'video_link': None
            }
        )

        # Проверка на то, что запись создалась в базе
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """ Тесты на список уроков """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('materials:lesson-list'))

        # Проверка на статус ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверка на верность структуры и полей в списке
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "title": "Test",
                        "course": None
                    }
                ]
            }
        )

    def test_detail_lesson(self):
        """ Тест на отображение деталей конкретного урока """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse("materials:lesson-detail", args=[1])
        )
        # Проверка на код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка на содержимое поля title
        self.assertEqual(response.data["title"], "Test")

    def test_update_lesson(self):
        """ Тесты на обновление данных урока """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test1',
            'description': 'Test1'
        }
        response = self.client.post(reverse('materials:lesson-create'), data=data)
        lesson_id = response.data['id']

        # Проверка, что владелец может вносить изменения
        self.client.force_authenticate(user=self.user)
        update_lesson = self.client.patch(
            reverse("materials:lesson-update", args=[lesson_id]),
            data={"title": "Updated title"}
        )
        # Проверка на статус ответа
        self.assertEqual(update_lesson.status_code, status.HTTP_200_OK)
        # Проверка на верность изменямых полей
        self.assertEqual(
            update_lesson.data["title"],
            "Updated title"
        )

        # Проверка на невозможность внесения изменений в урок, созданный другим пользователем
        self.client.force_authenticate(user=self.user2)
        update_lesson = self.client.patch(
            reverse("materials:lesson-update", args=[lesson_id]),
            data={"title": "Updated title"},
        )
        self.assertEqual(
            update_lesson.status_code, status.HTTP_403_FORBIDDEN
        )

    def test_delete_lesson(self):
        # Создание нового урока
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test1',
            'description': 'Test1',
        }
        response = self.client.post(reverse('materials:lesson-create'), data=data)
        lesson_id = response.data['id']

        # Проверка на невозможность удаления урока сторонним пользователем
        self.client.force_authenticate(user=self.user2)
        delete_lesson = self.client.delete(reverse('materials:lesson-delete', args=[lesson_id]))
        self.assertEqual(delete_lesson.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка на удаление урока владельцем
        self.client.force_authenticate(user=self.user)
        delete_lesson = self.client.delete(reverse('materials:lesson-delete', args=[lesson_id]))
        # Проверка статуса ответа
        self.assertEquals(
            delete_lesson.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверка отсутствия удаленного урока в базе
        get_deleted_lesson = self.client.get(reverse("materials:lesson-detail", args=[lesson_id]))
        self.assertEqual(
            get_deleted_lesson.status_code, status.HTTP_404_NOT_FOUND
        )


class SubscriptionTests(APITestCase):
    """ Тесты на эндпойнты подписки"""

    def setUp(self):
        self.user = User.objects.create(email="test@admin.pro", password="admin")
        self.course = Course.objects.create(
            title="Test",
            description="Test description",
            owner=self.user
        )

    def test_add_subscription(self):
        """ Проверка создания подписки """
        self.client.force_authenticate(user=self.user)
        data = {"user": self.user.id, "course": self.course.id}
        response = self.client.post(
            reverse("materials:subscription"), data=data
        )
        # Проверка кода ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверка подтверждающего сообщения
        self.assertEquals(
            response.json(),
            {'message': 'Вы подписались на курс'}
        )

    def test_2_destroy_subscription(self):
        """ Проверка удаления подписки """
        self.client.force_authenticate(user=self.user)
        data = {"user": self.user.id, "course": self.course.id}
        self.client.post(reverse("materials:subscription"), data=data
                         )
        # subscription_id = response.data['id']

        delete_response = self.client.post(
            reverse("materials:subscription"), data=data
        )
        print(delete_response.json())
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)
