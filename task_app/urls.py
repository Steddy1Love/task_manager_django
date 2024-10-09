from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  # path("task_app", views.task_app, name="task_app")
]