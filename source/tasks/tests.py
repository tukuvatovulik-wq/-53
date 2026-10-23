from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskPagesTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            description="Купить тетрадь",
            details="Зайти в магазин после школы.\nНе забыть клетку.",
            status="new",
        )

    def test_list_does_not_show_details(self):
        response = self.client.get(reverse("tasks:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Купить тетрадь")
        self.assertNotContains(response, "Зайти в магазин после школы")

    def test_detail_shows_task_fields_and_multiline_details(self):
        response = self.client.get(reverse("tasks:detail", args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Купить тетрадь")
        self.assertContains(response, "Зайти в магазин после школы.")
        self.assertContains(response, "Не забыть клетку.")

    def test_create_redirects_to_detail(self):
        response = self.client.post(reverse("tasks:create"), {
            "description": "Новая задача", "details": "Подробности",
            "status": "new", "due_date": "",
        })
        task = Task.objects.get(description="Новая задача")
        self.assertRedirects(response, reverse("tasks:detail", args=[task.pk]))
