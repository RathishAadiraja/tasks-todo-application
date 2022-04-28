from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField(null=True, blank=True)
    task_deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title

    class Meta:
        ordering = ['is_completed', 'task_deadline']