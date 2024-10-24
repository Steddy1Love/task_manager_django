from django.db import models

# Create your models here.

class TaskItem(models.Model):
  title = models.CharField(max_length=100)
  details = models.TextField(max_length=500)
  completed = models.BooleanField(default=False)
  recently_deleted = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)