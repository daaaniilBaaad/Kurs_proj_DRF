from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from atomic_habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        """Подготовка данных для тестов"""
        self.user = User.objects.create(email="admin@example.com")
        self.user.set_password("admin")
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            owner=self.user,
            time="00:01:00",
            period=2,
            action="Приседания",
        )

    def test_wont_create(self):
        """Тест на создание привычки"""
        url = reverse("atomic_habits:habits-create")
        data = {
            "place": "Test",
            "time": "00:01:00",
            "action": "Test",
            "period": 1,
        }
        response = self.client.post(url, data)
        print(datetime.now())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 2)

    def test_habit_list(self):
        """Тест на получение списка привычек"""
        url = reverse("atomic_habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.all().count(), 1)

    def test_wont_retrieve(self):
        """Тест на получение полей привычки по pk"""
        url = reverse("atomic_habits:habits-get", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_wont_update(self):
        """Тест на обновление полей привычки"""
        url = reverse("atomic_habits:habits-update", args=(self.habit.pk,))
        data_update = {
            "place": "Test",
            "action": "Test",
            "is_pleasant": "False",
            "period": 1,
            "award": "Test award",
            "time": "00:02:00",
        }
        response = self.client.patch(url, data=data_update)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("time"), "00:02:00")

    def test_wont_delete(self):
        """Тест на удаление привычки по pk"""
        url = reverse("atomic_habits:habits-delete", args={self.habit.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)
