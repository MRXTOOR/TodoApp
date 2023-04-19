from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Todo


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list':todos, 'title':'Главная страница', 'todo_list':todos})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    description = Todo(description=description)
    todo = Todo(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')