from django.db import models

# Create your models here.


class todoList(models.Model):
    task_name = models.CharField(max_length=400)
    created_at = models.DateTimeField(
        auto_now_add=True)
