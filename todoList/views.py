from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import todoList


def index(request):
    Context = todoList.objects.all()
    d = {
        'a': Context
    }
    return render(request, 'index.html', d)


def add(request):

    data = {
        'form': TaskForm
    }
    if request.method == 'POST':
        task_name = request.POST['task_name']
        d = todoList(task_name=task_name)
        d.save()
        return redirect('/')
    return render(request, 'delete.html', data)


def delete(request, task_name):
    t = todoList.objects.filter(task_name=task_name)
    t.delete()
    return redirect('/')


def update(request, task_name):
    data = {
        'form': TaskForm

    }
    if request.method == "POST":
        t = todoList.objects.filter(task_name=task_name)
        update_task_name = request.POST['task_name']
        t.update(task_name=update_task_name)
        return redirect('/')

    return render(request, 'update.html', data)


def search(request):
    search_data = request.GET['search_name']
    data = todoList.objects.filter(task_name__icontains=search_data)

    Context = {
        'd': data
    }
    return render(request, 'search.html', Context)
