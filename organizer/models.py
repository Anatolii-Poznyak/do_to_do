from django.db import models
from django.urls import reverse_lazy


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    done_mark = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["-done_mark", "-date"]
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return f"{self.name} created {self.date}"
