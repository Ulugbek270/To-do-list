from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from .forms import *
from django.contrib import messages


def index(request):
    return render(request, 'mynotes/index.html')


def tasks(request):
    tasks = Task.objects.all()
    active_tasks = Task.objects.filter(complete=False)
    inactive_tasks = Task.objects.filter(complete=True)[::-1][:6]
    numb_tasks = len(tasks)
    numb_active_tasks = len(active_tasks)
    numb_inactive_tasks = len(inactive_tasks)

    context = {
        'title': 'To-do list',
        'tasks': tasks,
        'numb_tasks': numb_tasks,

        'active_tasks': active_tasks,
        'inactive_tasks': inactive_tasks,

        'numb_inactive_tasks': numb_inactive_tasks,
        'numb_active_tasks': numb_active_tasks,

    }
    return render(request, 'mynotes/tasks.html', context)


def add_task(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New task added')
            return redirect('tasks')
        else:
            error = "There is nothing we can do"
    else:
        form = TaskForm()

    context = {
        'form': TaskForm(),
        'error': error,

    }
    return render(request, 'mynotes/tasks.html', context)


class TaskDelete(DeleteView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        messages.info(request, f'{task} deleted successfully')

        return redirect('tasks')


class TaskEdit(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'mynotes/edit_task.html'  # Для какой страницы класс
    success_url = reverse_lazy('tasks')


def toggle_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    messages.success(request, f'Good Job! Completing the task {task}')
    return redirect('tasks')


def untoggle_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = not task.complete
    task.save()
    messages.warning(request, f'So the task {task}, was not completed yet?')
    return redirect('tasks')
