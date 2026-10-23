from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by("id")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:detail", pk=task.pk)
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})
