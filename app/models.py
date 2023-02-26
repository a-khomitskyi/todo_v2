from django.db import models


task_priority = [
    (0, 'Звичайне'),
    (1, 'Помітне'),
    (2, 'Термінове'),
]


class TagModel(models.Model):
    tag_name = models.CharField(max_length=30)


class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(default=None, blank=True)
    priority = models.IntegerField(blank=True, choices=task_priority, default=0)
    completed = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField(TagModel, blank=True)