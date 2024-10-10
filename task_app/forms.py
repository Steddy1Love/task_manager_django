from django import forms
from .models import TaskItem

class TaskForm(forms.ModelForm):
  class Meta:
    model = TaskItem
    fields = ['title', 'details', 'completed']