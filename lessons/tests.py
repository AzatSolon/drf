from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lessons.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """
    Тест урока
    """

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@example.com")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Python", description="Python Test")
        self.lesson = Lesson.objects.create(
            course=self.course,
            title="test",
            description="DRF Test",
            owner=self.user,
            url="https://www.youtube.com/watch",
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        url = reverse("lessons:lessons_create")
        data = {
            "title": "test",
            "description": "DRF Test",
            "course": self.lesson.course.id,
            "url": "https://www.youtube.com/watch",
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(data.get("title"), "test")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("url"), "https://www.youtube.com/watch")
        self.assertEqual(data.get("description"), "DRF Test")

    def test_lesson_retrieve(self):
        self.url = reverse("lessons:lessons_retrieve", args=(self.lesson.pk,))
        self.data = {"title": "Основы программирования", "course": self.course.id}
        response = self.client.get(self.url)
        self.data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.lesson.title)
        self.assertEqual(response.data["course"], self.lesson.course.id)

    def test_lesson_update(self):
        self.url = reverse("lessons:lessons_update", args=(self.lesson.pk,))
        self.data = {
            "title": "Основы backend-разработки",
            "course": self.course.id,
            "description": "ООП",
        }
        response = self.client.put(self.url, self.data)
        self.data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Основы backend-разработки")
        self.assertEqual(response.data["course"], self.course.id)

    def test_lesson_delete(self):
        self.url = reverse("lessons:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    """Тестирование подписок"""

    def setUp(self):
        self.user = User.objects.create(email="admin1@localhost")
        self.course = Course.objects.create(title="Python", description="Основы Python")
        self.client.force_authenticate(user=self.user)
        self.url = reverse("lessons:subscription_create")

    def test_subscription_activate(self):
        """Тестирование активации подписки"""
        data = {"user": self.user.id, "course": self.course.id}
        response = self.client.post(self.url, data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(
            Subscription.objects.filter(user=self.user, course=self.course).exists(),
            True,
        )
        self.assertEqual(response.json().get("message"), "Подписка добавлена")

    def test_subscription_deactivate(self):
        """Тестирование деактивации подписки"""

        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.json(),
            {
                "message": "Подписка удалена",
            },
        )
        self.assertFalse(
            Subscription.objects.all().exists(),
        )
