from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("create_task/", views.create_task, name="create_task"),
  path("update_task/<int:pk>", views.update_task, name='update_task'),
]