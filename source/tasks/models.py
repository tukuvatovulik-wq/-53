from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("in_progress", "В процессе"),
        ("done", "Сделано"),
    ]

    description = models.TextField(verbose_name="Описание")
    details = models.TextField(blank=True, verbose_name="Подробное описание")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="new", verbose_name="Статус"
    )
    due_date = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return self.description
