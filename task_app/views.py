from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import TaskItem
# Create your views here.

def home(request):
  tasks = TaskItem.objects.all()
  return render(request, "home.html", {'tasks': tasks})

def create_task(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('create_task')
  else:
    form = TaskForm()
    return render(request, 'create_task.html', {'form': form})
  
def update_task(request, pk):
  task = get_object_or_404(TaskItem, pk=pk)
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = TaskForm(instance=task)
  return render(request, 'update_task.html', {'form': form})

def delete_task(request, pk):
  task = get_object_or_404(TaskItem, pk=pk)
  if request.method == 'DELETE':
    task.recently_deleted = True
    task.save()
  return redirect('home')

def recently_deleted(request):
  tasks = TaskItem.objects.get(recently_deleted==True)
  return render(request, 'recently_deleted.html', {'tasks': tasks})
